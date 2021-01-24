import RPi.GPIO as GPIO
from time import sleep

# while True:
#     GPIO.setmode(GPIO.BCM)
#     led = 24
#     GPIO.setup(led, GPIO.OUT)
#     GPIO.output(led, 4)
#     sleep(40)
#     GPIO.output(led, 0)
try:
   # GPIO.setmode(GPIO.BCM)
   # led = 24
   # GPIO.setup(led, GPIO.OUT)
   # GPIO.output(led, 4)
   # sleep(5)
   # GPIO.output(led, 0)
    while True:
        GPIO.setmode(GPIO.BCM)
        led = 21
        led2 = 26
        GPIO.setup(led, GPIO.OUT)
        GPIO.setup(led2, GPIO.OUT)
        GPIO.output(led, 4)
        sleep(4)
        GPIO.output(led, 0)
        GPIO.output(led2, 4)
        sleep(4)
        print('antes del sleep')
        GPIO.output(led2, 0)
        print('despues de apagar')
        sleep(4)
finally:
    print("Clean up")
    GPIO.cleanup() # cleanup all GPIO 
