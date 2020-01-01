#!/usr/bin/env python
import RPi.GPIO as GPIO

BtnPin = 13
Gpin   = 12
Rpin   = 11

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
    GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect)

def Led(x):
    if x == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)

def Print(x):
    if x == 0:
        print('    ***********************')
        print('    *   Button Pressed!   *')
        print('    ***********************')
    if x == 1:
        print('    ***********************')
        print('    *   Button Loosen!   *')
        print('    ***********************')

def detect(chn):
    Led(GPIO.input(chn))
    Print(GPIO.input(chn))

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
    except KeyboardInterrupt: 
        destroy()


