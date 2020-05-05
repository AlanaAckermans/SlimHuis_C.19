# usr/bin/python3
# Alana Ackermans
#23/04/2020

# LIBRARIES
import time
from signal import pause
from gpiozero import Button
from gpiozero import LED



def light_on():
    led_1.on()
        
def light_off():
    led_1.off()
    
def lights_status():
    if led_1.is_lit == True:
        led_1.off()
    else:
        led_1.on()
        

# VARIABLES
button_1 = Button(19)
button_2 = Button(13)
button_3 = Button(6)
button_4 = Button(5)

led_1 = LED(12)
led_2 = LED(16)
led_3 = LED(20)
led_4 = LED(21)

# START PROGRAM


button_1.when_pressed = lights_status
    
pause()
