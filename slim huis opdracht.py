# usr/bin/python3
# Alana Ackermans
#23/04/2020

# LIBRARIES
import time
from gpiozero import Button
from gpiozero import LED

# VARIABLES
button_1 = Button(19)
button_2 = Button(13)
button_3 = Button(6)
button_4 = Button(5)

# START PROGRAM

while True:
    
    if button_1.is_pressed:
        print("first button is pressed")
    if button_2.is_pressed:
        print("second button is pressed")
    if button_3.is_pressed:
        print("third button is pressed")
    if button_4.is_pressed:
        print("fourth button is pressed")