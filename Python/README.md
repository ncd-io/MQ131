
# About

This Library is intended for use with any MQ131 board available from ncd.io

### Developer information
NCD has been designing and manufacturing computer control products since 1995.  We have specialized in hardware design and manufacturing of Relay controllers for 20 years.  We pride ourselves as being the industry leader of computer control relay products.  Our products are proven reliable and we are very excited to support Particle.  For more information on NCD please visit ncd.io

### Requirements
- The Python SMBus Module: https://pypi.python.org/pypi/smbus-cffi/
- An I2C connection to MQ131 board
- Knowledge base for developing and programming with Python.

### Version
1.0.0

### How to use this library

The libary must be imported into your application and an I2C bus must be created with the SMBus module.

Once the library is imported and the I2C Bus created you can create a MQ131 object, pass it the I2C Bus and start to communicate to the chip.  You can optionally pass in a kwarg to the object that contains the address.

The default values for these configuration option are:
{'address': 0x50}

### Publicly accessible methods
```cpp
get_readings()
```
>This function returns the readings of the sensor.
