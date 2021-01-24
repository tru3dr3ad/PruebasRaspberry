import RPi.GPIO as GPIO
from time import sleep

try:
    while True:
        GPIO.setmode(GPIO.BCM)
        led = 21
        led1 = 26
        led2 = 20
        led3 = 16
        GPIO.setup(led, GPIO.OUT)
        GPIO.setup(led1, GPIO.OUT)
        GPIO.setup(led2, GPIO.OUT)
        GPIO.setup(led3, GPIO.OUT)
        GPIO.output(led, 4)
        GPIO.output(led3, 4)
        sleep(4)
        GPIO.output(led, 0)
        GPIO.output(led3, 0)
        GPIO.output(led2, 4)
        GPIO.output(led1, 4)
        sleep(4)
        print('antes del sleep')
        GPIO.output(led2, 0)
        GPIO.output(led1, 0)
        print('despues de apagar')
        sleep(4)
finally:
    print("Clean up")
    GPIO.cleanup() # cleanup all GPIO 
