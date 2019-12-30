#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


pins = {'pin_R': 11, 'pin_G': 12, 'pin_B': 15}
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
    GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
    
p_R = GPIO.PWM(pins['pin_R'], 55)  # set Frequece to 55Hz
p_G = GPIO.PWM(pins['pin_G'], 55)
p_B = GPIO.PWM(pins['pin_B'], 55)
    
p_R.start(100)      # Initial duty Cycle = 0(leds off)
p_G.start(100)
p_B.start(100)



try:
    color_list = list(range(0,100,5)) + list( range(100,0,-5) )
    i = 0
    size = len(color_list)
    while True:
        R = i % size
        G = (i+15) % size
        B = (i+30) % size
        
        p_R.ChangeDutyCycle(100 - color_list[R])
        p_G.ChangeDutyCycle(100 - color_list[G])
        p_B.ChangeDutyCycle(100 - color_list[B])
        time.sleep(0.35)
        
        p_R.ChangeDutyCycle(0)
        p_G.ChangeDutyCycle(0)
        p_B.ChangeDutyCycle(0)
        time.sleep(0.1)
        i = i+1
    
except KeyboardInterrupt:
    pass

p_R.stop()
p_G.stop()
p_B.stop()
GPIO.cleanup()

