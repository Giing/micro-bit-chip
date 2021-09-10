from microbit import *

i2c.init(100000)
addresses = i2c.scan()
print("-----OUT-----\n")
print("Adresses : ", addresses)
print(i2c.read(hex(addresses[0])))