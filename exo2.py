import machine, neopixel
from microbit import *

np = neopixel.NeoPixel(pin0, 1)

colors = {
    "blue": (0,0,60),
    "white": (60,60,60),
    "red": (60,0,0),
}

def change_color(color, sleep_time = 250):
    np[0] = colors[color]
    np.show()
    sleep(sleep_time)

while True:
    change_color("blue")
    change_color("white")
    change_color("red")