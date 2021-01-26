# from gpiozero import LEDBarGraph
# from time import sleep
# # from __future__ import division  # required for python 2

# graph = LEDBarGraph(20, 21, 16, 26, 12, 19)
# while True:
#     graph.value = 1  # (1, 1, 1, 1, 1, 1)
#     sleep(1)
#     graph.value = 1/2  # (1, 1, 1, 0, 0, 0)
#     sleep(1)
#     graph.value = -1/2  # (0, 0, 0, 1, 1, 1)
#     sleep(1)
#     graph.value = 1/4  # (1, 0, 0, 0, 0, 0)
#     sleep(1)
#     graph.value = -1  # (1, 1, 1, 1, 1, 1)
#     sleep(1)

from gpiozero import LEDBarGraph
from time import sleep
# from __future__ import division  # required for python 2

graph = LEDBarGraph(20, 21, 16, 26, 12, 19, pwm=True)

while True:
    graph.value = 1/10  # (0.5, 0, 0, 0, 0)
    sleep(1)
    graph.value = 3/10  # (1, 0.5, 0, 0, 0)
    sleep(1)
    graph.value = -3/10  # (0, 0, 0, 0.5, 1)
    sleep(1)
    graph.value = 9/10  # (1, 1, 1, 1, 0.5)
    sleep(1)
    graph.value = 95/100  # (1, 1, 1, 1, 0.75)