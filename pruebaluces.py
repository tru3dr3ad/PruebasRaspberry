import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 21
GPIO.setup(led, GPIO.OUT)
# Switch on
GPIO.output(led, 1)
# Switch off
GPIO.output(led, 0)