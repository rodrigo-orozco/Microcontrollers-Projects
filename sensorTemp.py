import machine
import utime

sensorTemp = machine.ADC(4)
conversionFactor= 3.3 / (65535)
sensorLm35 = machine.ADC(2)

tempInt = 0
tempExt = 0

button1 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
led1 = machine.Pin(15, machine.Pin.OUT)
led2 = machine.Pin(14, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)

def IntB1(Pin):
    # voltLm35 = sensorLm35.read_u16() * conversionFactor
    #  tempExt = voltLm35 / (0.010)
    sum = 0
    
    for i in range(1000):
        sum += (sensorLm35.read_u16() * conversionFactor) / (0.010)
    
    tempExt = sum / 1000
    
    print("The external temperature is: ", int(tempExt), "ºC")
    
    if int(tempExt) <= 30:
        led1.value(1)
        led2.value(0)
        led3.value(0)
    if int(tempExt) > 30 & int(tempExt) < 40:
        led1.value(0)
        led2.value(1)
        led3.value(0)
    if int(tempExt) >= 40:
        led1.value(0)
        led2.value(0)
        led3.value(1)
        
def IntB2(Pin):
    
    #tempInt = 27 - (voltTmp - 0.706)/0.001721
    sum = 0
    
    for i in range(1000):
        voltTmp = sensorTemp.read_u16() * conversionFactor
        sum += 27 - (voltTmp - 0.706) / (0.001721)
    
    tempInt = sum / 1000
    
    print("The internal temperature is: ", int(tempInt), "ºC")
    
    if int(tempInt) <= 30:
        led1.value(1)
        led2.value(0)
        led3.value(0)
    if int(tempInt) > 30 & int(tempInt) < 40:
        led1.value(0)
        led2.value(1)
        led3.value(0)
    if int(tempInt) >= 40:
        led1.value(0)
        led2.value(0)
        led3.value(1)

print("""Do you want to visualize Internal or External Temperature?
            Press Button 1 for External Temperature.
            Press Button 2 for Internal Temperature.""")

button1.irq(handler=IntB1, trigger=machine.Pin.IRQ_FALLING)
button2.irq(handler=IntB2, trigger=machine.Pin.IRQ_FALLING)