from gpiozero import Button, LED
from time import sleep
import random

led = LED(21)

player_1 = Button(2)
player_2 = Button(3)

time = random.uniform(5, 10)
sleep(time)
led.on()

while True:
    if player_1.is_pressed:
        print("Pin2 wins!")
        break
    if player_2.is_pressed:
        print("Pin3 wins!")
        break

led.off()