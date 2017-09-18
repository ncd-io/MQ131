import time
import smbus
import mq131
# Get I2C bus, this is I2C Bus 1
bus = smbus.SMBus(1)
#kwargs is a Python set that contains the address of your device as well as additional device and calibration values.
#kwargs does not have to be populated as every value is optional and will be replaced with a default value if not is specified.
#kwargs does however need to be instantiated as a set such as below
kwargs = {}

#below is an example of a kwarg declaration that is populated with all of the default values for each user configurable property
#refer to the datasheet for this chip to calculate what values you should be using for your project.
#For instance if you are using light pipes you would want to alter glass atennuation.
kwargs = {'address': 0x50}
#create the MQ131 object from the MQ131 library
#the object requires that you pass it the bus object so that it can communicate and share the bus with other chips if necessary
mq131 = mq131.MQ131(bus, kwargs)

while True :
    print mq131.take_readings()
    time.sleep(.25)
