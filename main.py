import py_compile

from slider import Slider
from queue import Queue

list = [8, 7, 1, 6, 9, 2, 5, 4, 3]

x = Slider()
x.input(list)
q = Queue()

a = q.uniform_search(x)
x.followPathDetailed(a.getPath())