from slider import Slider
import copy

class Search:
    def __init__(self, Slider):
        self.nodes = []
        self.pastDict = {}
        self.origin = Slider
        self.name = ""

    def search(self):
        self.nodes.append(self.origin)
        numParsed = 0
        while(True):
            if not self.nodes:
                return self.origin
            current = self.nodes.pop(0)
            numParsed += 1
            if current.isCorrect():
                print (self.getName() + " checked through " + str(numParsed) + " states and found a solution at depth " + str(current.getDepth()) + ".")
                return current
            self.queue(current)

    def inPast(self, Slider):
        return Slider.getHash() in self.pastDict

    def getIndex(self, value):
        for i in range(len(self.nodes)):
            if self.pastDict[self.nodes[i].getHash()] > value:
                return int(i)
        return len(self.nodes)-1

    def queue(self, Slider):
        up = copy.deepcopy(Slider)
        if up.moveUp():
            self.appendToQueue(up)
        down = copy.deepcopy(Slider)
        if down.moveDown():
            self.appendToQueue(down)
        left = copy.deepcopy(Slider)
        if left.moveLeft():
            self.appendToQueue(left)
        right = copy.deepcopy(Slider)
        if right.moveRight():
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
            self.nodes.insert(self.getIndex(heuristicValue), Slider)