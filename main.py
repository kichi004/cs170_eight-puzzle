import py_compile

from slider import Slider
from queue import Queue

list = [8, 7, 1, 6, 9, 2, 5, 4, 3]

x = Slider()
x.input(list)
y = Slider()
y.input(list)
z = Slider()
z.input(list)

u = Queue()
i = Queue()
a = Queue()
# '''
ua = u.uniform_search(x)
ua.printGrid()
print(ua.getPath())
print(len(ua.getPath()))
x.followPathDetailed(ua.getPath())
'''
ia = i.misplaced_search(y)
ia.printGrid()
print(ia.getPath())
print(len(ia.getPath()))
y.followPathDetailed(ia.getPath())

aa = a.manhattan_search(z)
aa.printGrid()
print(aa.getPath())
print(len(aa.getPath()))
z.followPathDetailed(aa.getPath())
'''