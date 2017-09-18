class MQ131():
    def __init__(self, smbus, kwargs = {}):
        self.__dict__.update(kwargs)
        if not hasattr(self, 'address'):
            self.address = 0x50
        self.smbus = smbus

    def take_readings(self):
        reading = self.smbus.read_i2c_block_data(self.address, 0x00, 2)
        reading = ((reading[0] & 0x0F) << 8) + reading[1]
        real_reading = (1.99 * reading) / 4095.0 + 0.01
        return real_reading
