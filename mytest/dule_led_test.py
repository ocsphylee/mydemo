#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = {'pin_R':11, 'pin_G':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
    GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 50)  # set Frequece to 200Hz
p_G = GPIO.PWM(pins['pin_G'], 50)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)


try:
    while True:
        for dc in range(0,101,5):
            p_R.ChangeDutyCycle(dc)
            p_G.ChangeDutyCycle(100-dc)
            time.sleep(0.1)
        for dc in range(100,-1,-5):
            p_R.ChangeDutyCycle(dc)
            p_G.ChangeDutyCycle(100-dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p_R.stop()
p_G.stop()
GPIO.cleanup()
