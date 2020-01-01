#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

VibratePin = 13
Gpin   = 12
Rpin   = 11

state = 0

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
    GPIO.setup(VibratePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.add_event_detect(VibratePin, GPIO.BOTH, callback=detect,bouncetime=200)




def Led(x):
    global state
    if state == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    else: 
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)
    state = 1- state
    
def Print(x):
    if state == 0:
        print( '    **********')
        print( '    *     ON *')
        print( '    **********')

    else:
        print( '    **********')
        print( '    * OFF    *')
        print( '    **********')
    
    
def detect(channel):
    Led(GPIO.input(channel))
    Print(GPIO.input(channel))
    
def loop():

    while True:
        pass
            

def destroy():
    GPIO.output(Gpin, GPIO.HIGH)       # Green led off
    GPIO.output(Rpin, GPIO.HIGH)       # Red led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()