import py_compile

from slider import Slider
from queue import Queue

list = [1, 2, 3, 4, 5, 6, 7, 9, 8]

x = Slider()
x.input(list)

y = Slider()
y.copy(x)

y.printGrid()