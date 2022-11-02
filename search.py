from slider import Slider
import copy

class GeneralSearch:
    def __init__(self, Slider):
        self.queue = [] # queue of states to examine
        self.pastDict = {} # previously visited states
        self.initialState = Slider # initial state to trace from later
        self.numParsed = 0 # number of parsed states
        self.maxQueueSize = 0 # maximum queue size achieved

    def search(self): # general search algorithm 
        self.pastDict[self.initialState.getHash()] = True
        self.queue.append(self.initialState)
        self.numParsed = 0
        while(True):
            if len(self.queue) > self.maxQueueSize:
                self.maxQueueSize = len(self.queue)
            if not self.queue:
                print (self.getName() + " checked through " + str(self.numParsed) + " states and failed to find a solution.\n")
                print("Max queue size: " + str(self.maxQueueSize) + "\n")
                return self.initialState
            current = self.queue.pop(0)
            self.numParsed += 1
            if current.isCorrect():
                print (self.getName() + " checked through " + str(self.numParsed) + " states and found a solution at depth " + str(current.getDepth()) + ".")
                return current
            self.expand(current)

    def inPast(self, Slider): # returns true if the game state can be found in the past dictionary
        return Slider.getHash() in self.pastDict

    def getIndex(self, value): # returns the index of the state's correct position in the queue
        for i in range(len(self.queue)):
            if (self.getPriorityValue(self.queue[i])) > value:
                return int(i)
        return len(self.queue)

    def expand(self, Slider): # attempts all 4 operations on a state and queues them
        up = copy.deepcopy(Slider)
        if up.moveUp(): # movement functions return false if the move is not legal 
            self.queueingFunction(up)
        down = copy.deepcopy(Slider)
        if down.moveDown():
            self.queueingFunction(down)
        left = copy.deepcopy(Slider)
        if left.moveLeft():
            self.queueingFunction(left)
        right = copy.deepcopy(Slider)
        if right.moveRight():
            self.queueingFunction(right)

    def followSolution(self, route): # follows the path of the solution to write a traceback
        path = route
        print("\nThe initial state of the puzzle is...")
        solutionFollower = copy.deepcopy(self.initialState)
        solutionFollower.print()
        while (len(path) != 0):
            direction = path[0]
            solutionFollower = solutionFollower.followPath(direction)
            print("The best state to expand with a g(n) = " + str(solutionFollower.getDepth()) + self.getHeuristicStatement(solutionFollower) + " is...")
            solutionFollower.print()
            path = path[1:]
        print("Goal State!\n")
        print("Solution depth was " + str(len(route)) + ", taking the path " + str(route) + ".")
        print("Number of nodes expanded: " + str(self.numParsed))
        print("Max queue size: " + str(self.maxQueueSize) + "\n")

class UniformSearch(GeneralSearch):
    def getName(self):  # returns name for print statement
        return "Uniform Cost Search"

    def getPriorityValue(self, Slider): # normally returns h(n) + g(n), unused for uniform search 
        return True

    def getHeuristicStatement(self, Slider): # also unused for uniform search
        return ""
    
    def queueingFunction(self, Slider): # confirms if already checked, then appends new state to the queue
        if not self.inPast(Slider):
            self.pastDict[Slider.getHash()] = True
            self.queue.append(Slider)

class MisplacedSearch(GeneralSearch):
    def getName(self): # return name for print statement
        return "Misplaced Tile Heuristic"

    def getPriorityValue(self, Slider): # returns h(n) + g(n) named "priority value"
        return Slider.getMisplacedTilesPriorityValue()
    
    def getHeuristicStatement(self, Slider): # returns string statement for traceback
        return " and h(n) = " + str(Slider.getMisplacedTilesHeuristic())

    def queueingFunction(self, Slider): # adds to queue, asking the getIndex function for correct spot
        if not self.inPast(Slider):
            self.pastDict[Slider.getHash()] = True
            self.queue.insert(self.getIndex(self.getPriorityValue(Slider)), Slider)

class ManhattanSearch(GeneralSearch):
    def getName(self): # returns name for print statement
        return "Manhattan Distance Heuristic"

    def getPriorityValue(self, Slider): # return h(n) + g(n) named "priority value"
        return Slider.getManhattanDistancePriorityValue()

    def getHeuristicStatement(self, Slider): # returns string statement for traceback
        return " and h(n) = " + str(Slider.getManhattanDistanceHeuristic())

    def queueingFunction(self, Slider): #adds to queue, asking the getIndex function for correct spot
        if not self.inPast(Slider):
            self.pastDict[Slider.getHash()] = True
            self.queue.insert(self.getIndex(self.getPriorityValue(Slider)), Slider)