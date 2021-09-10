from microbit import *

uart.init(115200)
while True :
    uart.write("\n" + str(temperature()) + "\n")
    sleep(1000)