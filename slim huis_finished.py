# usr/bin/python3
# Alana Ackermans
#23/04/2020

# LIBRARIES
import time
from signal import pause
from gpiozero import Button
from gpiozero import LED


#LISTS
buttons = [Button(19), Button(13), Button(6), Button(5)]
leds = [LED(12), LED(16), LED(20), LED(21)]


# START PROGRAM
while True:
    i = 0
    while i < 4:
        if buttons[i].is_pressed == True:
            if leds[i].is_lit == True:
                leds[i].off()
                time.sleep(0.5)
            else:
                leds[i].on()
                time.sleep(0.5)
        i += 1
    
pause()
 