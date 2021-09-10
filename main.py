from microbit import *
# display.scroll("Hello, World!")
# nb_left = 0
compass.calibrate()
while True :
    # Exo 4
    # if button_a.is_pressed() :
    #    display.scroll("Pressed ! ")

    # if button_b.is_pressed() :
    #    display.scroll("Mathis le caca! ")

    # Exo 5
    # if temperature() > 30 :
    #    display.scroll("/!\ Danger temp " + str(temperature()))
    # else :
    #    display.scroll("OK " + str(temperature()))

    # Exo 6
    # if accelerometer.current_gesture() == "left" and not accelerometer.was_gesture("left") :
    #    nb_left += 1

    # display.show(str(nb_left))

    # Exo 7
    aiguille = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[aiguille])