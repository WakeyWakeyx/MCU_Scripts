from time import sleep, time

#globals
temp_add = 0x38
sda = Pin(11, mode=Pin.OPEN_DRAIN, pull=Pin.PULL_UP)
scl = Pin(12, mode=Pin.OPEN_DRAIN,pull=Pin.PULL_UP)
i2c = I2C(sda=sda, scl=scl)

#functions
def read_temp() -> None:
    sleep(0.01)
    i2c.writeto(temp_add,bytes([0xAC,0x30,0x00]))
    sleep(0.25)
    data = (i2c.readfrom(temp_add,7))

    read_status = data[0] >> 7
    if(read_status):
        return None

    humidity_bytes = (data[1]<<12) | (data[2]<<4) | (data[3]>>4)
    temp_byte = (data[3]&0x0F)<<16 | (data[4] << 8) | data[5]
    temperature = temp_byte * 200.0 / 0x100000 - 50
    humidity = 100*humidity_bytes/0x100000
    print(f'the temp: {temperature:.2f}')
    print(f'the humidity: {humidity:.2f}%')
