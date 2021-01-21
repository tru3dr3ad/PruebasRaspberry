from gpiozero import PWMLED
from time import sleep

led = PWMLED(21)

while True:
    led.value = 0  # off
    sleep(1)
    led.value = 0.5  # half brightness
    sleep(1)
    led.value = 1  # full brightness
    sleep(1)
    gpiozero.clear()
