from slider import Slider
import copy

class Search:
    def __init__(self, Slider):
        self.nodes = []
        self.pastDict = {}
        self.origin = Slider
        self.name = ""
        self.parsed = 0
        self.maxQueueSize = 0

    def search(self):
        self.pastDict[self.origin.getHash()] = self.makeHeuristicValue(self.origin)
        self.nodes.append(self.origin)
        numParsed = 0
        while(True):
            if len(self.nodes) > self.maxQueueSize:
                self.maxQueueSize = len(self.nodes)
            if not self.nodes:
                print (self.getName() + " checked through " + str(numParsed) + " states and failed to find a solution.\n")
                return self.origin
            current = self.nodes.pop(0)
            numParsed += 1
            if current.isCorrect():
                print (self.getName() + " checked through " + str(numParsed) + " states and found a solution at depth " + str(current.getDepth()) + ".")
                self.parsed = numParsed
                return current
            # print("current is " + current.getPath(), end=", ")
            self.queue(current)

    def inPast(self, Slider):
        return Slider.getHash() in self.pastDict

    def getIndex(self, value):
        for i in range(len(self.nodes)):
            if (self.makeHeuristicValue(self.nodes[i])) > value:
                return int(i)
        return len(self.nodes)

    def findLowest(self):
        for i in self.nodes:
            print(str(self.makeHeuristicValue(i)),end=", ")

    def queue(self, Slider):
        up = copy.deepcopy(Slider)
        if up.moveUp():
            #print(self.makeHeuristicValue(up), end="!")
            self.appendToQueue(up)
        down = copy.deepcopy(Slider)
        if down.moveDown():
            #print(self.makeHeuristicValue(down), end="!")
            self.appendToQueue(down)
        left = copy.deepcopy(Slider)
        if left.moveLeft():
            #print(self.makeHeuristicValue(left), end="!")
            self.appendToQueue(left)
        right = copy.deepcopy(Slider)
        if right.moveRight():
            #print(self.makeHeuristicValue(right), end="!")
            self.appendToQueue(right)

    def followSolution(self, route):
        path = route
        print("\nThe initial state of the puzzle is...")
        holder = copy.deepcopy(self.origin)
        holder.printGrid()
        while (len(path) != 0):
            direction = path[0]
            holder = holder.followPath(direction)
            print("The best state to expand with a g(n) = " + str(holder.getDepth()) + self.getHeuristicStatement(holder) + " is...")
            holder.printGrid()
            path = path[1:]
        print("Goal State!\n")
        print("Solution depth was " + str(len(route)) + ", taking the path " + str(route) + ".")
        print("Number of nodes expanded: " + str(self.parsed))
        print("Max queue size: " + str(self.maxQueueSize) + "\n")

class UniformSearch(Search):
    def getName(self):
        return "Uniform Cost Search"

    def makeHeuristicValue(self, Slider):
        return True

    def getHeuristicStatement(self, Slider):
        return ""
    
    def appendToQueue(self, Slider):
        if not self.inPast(Slider):
            self.pastDict[Slider.getHash()] = self.makeHeuristicValue(Slider)
            self.nodes.append(Slider)

class MisplacedSearch(Search):
    def getName(self):
        return "Misplaced Tile Heuristic"

    def makeHeuristicValue(self, Slider):
        return Slider.getMisplacedTilesHeuristic()
    
    def getHeuristicStatement(self, Slider):
        return " and h(n) = " + str(Slider.getMisplacedTiles())

    def appendToQueue(self, Slider):
        if not self.inPast(Slider):
            heuristicValue = self.makeHeuristicValue(Slider)
            self.pastDict[Slider.getHash()] = heuristicValue
            self.nodes.insert(self.getIndex(heuristicValue), Slider)

class ManhattanSearch(Search):
    def getName(self):
        return "Manhattan Distance Heuristic"

    def makeHeuristicValue(self, Slider):
        return Slider.getManhattanHeuristic()

    def getHeuristicStatement(self, Slider):
        return " and h(n) = " + str(Slider.getManhattanDistance())

    def appendToQueue(self, Slider):
        if not self.inPast(Slider):
            heuristicValue = self.makeHeuristicValue(Slider)
            self.pastDict[Slider.getHash()] = heuristicValue
            # print(self.getIndex(heuristicValue), end="@")
            self.nodes.insert(self.getIndex(heuristicValue), Slider)