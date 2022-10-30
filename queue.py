from asyncore import loop
from slider import Slider
import copy

class Queue:
    def __init__(self):
        self.nodes = []
        self.dict = {}
    
    def wasInPast(self, Slider):
        return self.dict.get(Slider.makeHash())

    def queue(self, Slider):
        u = copy.deepcopy(Slider)
        if u.moveUp():
            if not self.wasInPast(u):
                self.nodes.append(u)
        d = copy.deepcopy(Slider)
        if d.moveDown():
            if not self.wasInPast(d):
                self.nodes.append(d)
        l = copy.deepcopy(Slider)
        if l.moveLeft():
            if not self.wasInPast(l):
                self.nodes.append(l)
        r = copy.deepcopy(Slider)
        if r.moveRight():
            if not self.wasInPast(r):
                self.nodes.append(r)

    def uniform_search(self, Slider):
        self.nodes.append(Slider)
        checked = 0
        while(True):
            if not self.nodes:
                print("Queue is empty, failure.")
            curr = self.nodes.pop(0)
            if curr.checkCorrect():
                return curr
            self.dict[curr.makeHash()] = True
            checked += 1
            print(checked)
            self.queue(curr)


