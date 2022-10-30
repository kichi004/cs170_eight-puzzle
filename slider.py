import math

from operator import truediv

class Slider:
    def __init__(self):
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # array representing the game board, 9 = blank
        self.len = 3  # side length of the array
        self.pos = 8  # position of the blank
        self.path = ""  # string to track previous actions taken

    def swapPositions(self, pos1, pos2):
        store = self.list[pos1]
        self.list[pos1] = self.list[pos2]
        self.list[pos2] = store

    def checkCorrect(self):
        prev = 0
        for i in range(len(self.list)):
            if (self.list[i] > prev):
                prev += 1
            else:
                return False
        return True

    def input(self, olist):
        self.list = olist
        self.path = ""
        self.pos = self.findBlank()
        self.len = math.sqrt(len(self.list))

    def getList(self):
        return self.list

    def equalsList(self, olist):
        if (olist == self.list):
            return True
        else:
            return False

    def findBlank(self):
        blankPos = 0
        for i in range(len(self.list)):
            if self.list[blankPos] < self.list[i]:
                blankPos = i
        return blankPos

    def copy(self, Slider):
        self.list = Slider.list
        self.len = Slider.len
        self.pos = Slider.pos
        self.path = Slider.path

    def printGrid(self):
        cnt = 1
        print("[[", end="")
        for x in range(len(self.list)):
            cnt += 1
            if x == self.pos:
                print("X", end="")
            else:
                print(self.list[x], end="")
            if cnt > self.len:
                print("]", end="")
                cnt = 1
                if (x+1 != len(self.list)):
                    print()
                    print(" [", end="")
            else:
                print(", ", end="")
        print("]", end="\n\n")

    def checkBounds(self, p):
        if (p > len(self.list)-1):
            return False
        elif (p < 0):
            return False
        else:
            return True
    
    def moveUp(self):
        newPos = self.pos-3
        if (self.checkBounds(newPos)):
            self.swapPositions(self.pos, newPos)
            self.pos = newPos
            self.path += "U"
            return True
        else: 
            return False
    
    def moveDown(self):
        newPos = self.pos+3
        if (self.checkBounds(newPos)):
            self.swapPositions(self.pos, newPos)
            self.pos = newPos
            self.path += "D"
            return True
        else: 
            return False

    def moveLeft(self):
        newPos = self.pos-1
        if (self.pos%self.len!=0):
            self.swapPositions(self.pos, newPos)
            self.pos = newPos
            self.path += "L"
            return True
        else: 
            return False
    
    def moveRight(self):
        newPos = self.pos+1
        if (self.pos%self.len != (self.len-1)):
            self.swapPositions(self.pos, newPos)
            self.pos = newPos
            self.path += "R"
            return True
        else: 
            return False

    def getPath(self):
        return self.path
    
    def followPath(self, route):
        for i in range(len(route)):
            if (route[i] == "U"):
                self.moveUp()
            elif (route[i] == "D"):
                self.moveDown()
            elif (route[i] == "L"):
                self.moveLeft()
            elif (route[i] == "R"):
                self.moveRight()
            else:
                return False
        return True

    def followPathDetailed(self, route):
        print("Initial State:")
        self.printGrid()
        for i in range(len(route)):
            if (route[i] == "U"):
                self.moveUp()
                print("Move #" + str(i+1) + ": ")

                print("Move Blank Upwards")
                self.printGrid()
            elif (route[i] == "D"):
                self.moveDown()
                print("Move #" + str(i+1) + ": ")
                print("Move Blank Downwards")
                self.printGrid()
            elif (route[i] == "L"):
                self.moveLeft()
                print("Move #" + str(i+1) + ": ")
                print("Move Blank Left")
                self.printGrid()
            elif (route[i] == "R"):
                self.moveRight()
                print("Move #" + str(i+1) + ": ")
                print("Move Blank Right")
                self.printGrid()
            else:
                return False
        return True



    
