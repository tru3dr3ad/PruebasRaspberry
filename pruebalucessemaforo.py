from gpiozero import LED
from time import sleep
  

red = LED(2)
#amber = LED(3)
#green = LED(4)

#green.on()
#amber.on()
red.on()
sleep(10)


while True:
  red.on()
#   red.on()
#   sleep(2)
#   red.off()

 #       green.on()
   #     amber.on()
    #    amber.off()
  #      red.on()
        # sleep(10)
        # green.off()
        # amber.on()
        # sleep(1)
        # amber.off()
        # red.on()
        # sleep(10)
        # amber.on()
        # sleep(1)
        # green.on()
        # amber.off()
        # red.off()
