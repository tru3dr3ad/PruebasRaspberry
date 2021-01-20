import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BCM)
    led = 21
    GPIO.setup(led, GPIO.OUT)
    # Switch on
    GPIO.output(led, 1)
    # Switch off
    GPIO.output(led, 0)
finally:
       print("clean up") 
          GPIO.cleanup() # cleanup all GPIO 
