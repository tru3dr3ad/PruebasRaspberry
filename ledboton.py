from gpiozero import LED, Button, LEDBoard
from signal import pause

led = LEDBoard(20,21,26,16)
button = Button(2)

button.when_pressed = led.on
# button.when_pressed = led1.on
button.when_released = led.off
# button.when_released = led1.off


pause()