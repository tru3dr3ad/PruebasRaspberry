from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

button_sounds = {
    Button(2): Sound("/gpio-music-box/1.wav"),
    Button(3): Sound("/gpio-music-box/2.wav"),
}

for button, sound in button_sounds.items():
    button.when_pressed = sound.play

pause()