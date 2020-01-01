import RPi.GPIO as GPIO


reed = 12
Buzzer = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(reed, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Buzzer, GPIO.OUT)
Buzz = GPIO.PWM(Buzzer, 1)
Buzz.start(50)


        
def detect(chn):
    if GPIO.input(reed):
        Buzz.ChangeFrequency(1)
        
    else:
        Buzz.ChangeFrequency(480)
        print('    ***********************************')
        print( '    *   Detected Magnetic Material!   *')
        print( '    ***********************************')
        
GPIO.add_event_detect(reed, GPIO.BOTH, callback=detect, bouncetime=1000)
try:
    while True:
        pass
except KeyboardInterrupt:   # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    Buzz.stop()                 # Stop the buzzer
    GPIO.output(Buzzer, 1)      # Set Buzzer pin to High
    GPIO.cleanup()