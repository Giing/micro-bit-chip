from microbit import *
while True :
    # display.show(pin0.read_analog())
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    switch:
    sleep(2000)
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    display.show(Image.HAPPY)
    sleep(2000)
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(500)