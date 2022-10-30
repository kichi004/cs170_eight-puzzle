from asyncore import loop
from slider import Slider
import copy

class Queue:
    def __init__(self):
        self.nodes = []
        self.dict = {}
    
    def wasInPast(self, Slider):
        return Slider.makeHash() in self.dict
    
    def indexIncrement(self, val):
        for i in range(len(self.nodes)):
            if self.dict[self.nodes[i].makeHash()] >= val:
                return int(i)
        return len(self.nodes)-1

    def queueUniform(self, Slider):
        u = copy.deepcopy(Slider)
        if u.moveUp():
            if not self.wasInPast(u):
                self.nodes.append(u)
                self.dict[u.makeHash()] = True
        d = copy.deepcopy(Slider)
        if d.moveDown():
            if not self.wasInPast(d):
                self.nodes.append(d)
                self.dict[d.makeHash()] = True
        l = copy.deepcopy(Slider)
        if l.moveLeft():
            if not self.wasInPast(l):
                self.nodes.append(l)
                self.dict[l.makeHash()] = True
        r = copy.deepcopy(Slider)
        if r.moveRight():
            if not self.wasInPast(r):
                self.nodes.append(r)
                self.dict[r.makeHash()] = True

    def queueMisplaced(self, Slider):
        u = copy.deepcopy(Slider)
        if u.moveUp():
            if not self.wasInPast(u):
                uHeu = u.getMisplacedTilesHeuristic()
                self.dict[u.makeHash()] = uHeu
                self.nodes.insert(self.indexIncrement(uHeu), u)
        d = copy.deepcopy(Slider)
        if d.moveDown():
            if not self.wasInPast(d):
                dHeu = d.getMisplacedTilesHeuristic()
                self.dict[d.makeHash()] = dHeu
                self.nodes.insert(self.indexIncrement(dHeu), d)
        l = copy.deepcopy(Slider)
        if l.moveLeft():
            if not self.wasInPast(l):
                lHeu = l.getMisplacedTilesHeuristic()
                self.dict[l.makeHash()] = lHeu
                self.nodes.insert(self.indexIncrement(lHeu), l)
        r = copy.deepcopy(Slider)
        if r.moveRight():
            if not self.wasInPast(r):
                rHeu = r.getMisplacedTilesHeuristic()
                self.dict[r.makeHash()] = rHeu
                self.nodes.insert(self.indexIncrement(rHeu), r)

    def queueManhattan(self, Slider):
        u = copy.deepcopy(Slider)
        if u.moveUp():
            if not self.wasInPast(u):
                uHeu = u.getManhattanHeuristic()
                self.dict[u.makeHash()] = uHeu
                self.nodes.insert(self.indexIncrement(uHeu), u)
        d = copy.deepcopy(Slider)
        if d.moveDown():
            if not self.wasInPast(d):
                dHeu = d.getManhattanHeuristic()
                self.dict[d.makeHash()] = dHeu
                self.nodes.insert(self.indexIncrement(dHeu), d)
        l = copy.deepcopy(Slider)
        if l.moveLeft():
            if not self.wasInPast(l):
                lHeu = l.getManhattanHeuristic()
                self.dict[l.makeHash()] = lHeu
                self.nodes.insert(self.indexIncrement(lHeu), l)
        r = copy.deepcopy(Slider)
        if r.moveRight():
            if not self.wasInPast(r):
                rHeu = r.getManhattanHeuristic()
                self.dict[r.makeHash()] = rHeu
                self.nodes.insert(self.indexIncrement(rHeu), r)

    def uniform_search(self, Slider):
        self.nodes.append(Slider)
        checked = 0
        while(True):
            if not self.nodes:
                print("Queue is empty, failure.")
            curr = self.nodes.pop(0)
            if curr.checkCorrect():
                return curr
            checked += 1
            #print(checked)
            # print(len(self.nodes))
            self.queueUniform(curr)
    
    def misplaced_search(self, Slider):
        self.nodes.append(Slider)
        checked = 0
        while(True):
            if not self.nodes:
                print("Queue is empty, failure.")
            curr = self.nodes.pop(0)
            if curr.checkCorrect():
                return curr
            checked += 1
            #print(checked)
            # print(len(self.nodes))
            self.queueMisplaced(curr)

    def manhattan_search(self, Slider):
        self.nodes.append(Slider)
        checked = 0
        while(True):
            if not self.nodes:
                print("Queue is empty, failure.")
            curr = self.nodes.pop(0)
            if curr.checkCorrect():
                return curr
            checked += 1
            #print(checked)
            # print(len(self.nodes))
            self.queueManhattan(curr)

