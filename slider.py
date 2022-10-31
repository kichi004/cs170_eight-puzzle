import math

from operator import truediv

class Slider:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # array representing the game board, highest value = blank
        self.len = 3  # side length of the array
        self.pos = 8  # position of the blank
        self.path = ""  # string to track previous actions taken
    
    def __init__(self, board): # alternate initialization to add custom board state
        pass
        self.input(board)

    def swap(self, pos1, pos2): # swaps the position of two tiles, no checks involved
        store = self.board[pos1]
        self.board[pos1] = self.board[pos2]
        self.board[pos2] = store

    def isCorrect(self): # checks if the board is correct
        prev = 0
        for i in self.board:
            if (i > prev):
                prev += 1
            else:
                return False
        return True

    def input(self, newBoard): # used to input a custom board into an already existing slider
        self.board = newBoard
        self.path = ""
        self.pos = self.findBlankPosition()
        self.len = math.sqrt(len(self.board))

    def getBoard(self): # returns the board state as a list object
        return self.board

    def isEqual(self, newBoard): # checks if the list objects of two boards are equal, no other checks
        if (newBoard == self.board):
            return True
        else:
            return False

    def findBlankPosition(self): # finds the highest value in the list to determine the blank position, does not set
        blankPosition = 0
        for i in range(len(self.board)):
            if self.board[blankPosition] < self.board[i]:
                blankPosition = i
        return blankPosition

    def printGrid(self): # prints the grid, adaptive for different sizes but doesn't look great with double digits
        cnt = 1
        print("[[", end="")
        for x in range(len(self.board)):
            cnt += 1
            if x == self.pos:
                print("X", end="")
            else:
                print(self.board[x], end="")
            if cnt > self.len:
                print("]", end="")
                cnt = 1
                if (x+1 != len(self.board)):
                    print()
                    print(" [", end="")
            else:
                print(", ", end="")
        print("]", end="\n\n")

    def checkBounds(self, p): # makes sure that the new position on the board does not go outside of the range of the list
        if (p > len(self.board)-1):
            return False
        elif (p < 0):
            return False
        return True
    
    def moveUp(self): # moves the blank up by subtracting 3 
        newPos = self.pos-3
        if (self.checkBounds(newPos)):
            self.swap(self.pos, newPos)
            self.pos = newPos
            self.path += "U"
            return True
        else: 
            return False
    
    def moveDown(self): # moves the blank down by adding 3
        newPos = self.pos+3
        if (self.checkBounds(newPos)):
            self.swap(self.pos, newPos)
            self.pos = newPos
            self.path += "D"
            return True
        else: 
            return False

    def moveLeft(self): # moves the blank left by subtracting 1
        newPos = self.pos-1
        if (self.pos%self.len!=0):
            self.swap(self.pos, newPos)
            self.pos = newPos
            self.path += "L"
            return True
        else: 
            return False
    
    def moveRight(self): # moves the blank right by subtracting 1
        newPos = self.pos+1
        if (self.pos%self.len != (self.len-1)):
            self.swap(self.pos, newPos)
            self.pos = newPos
            self.path += "R"
            return True
        else: 
            return False

    def getPath(self): # returns the string path of the moves the slider object has taken so far
        return self.path
    
    def followPath(self, direction): # follows the directional string of another object 
        if (direction == "U"):
            self.moveUp()
        elif (direction == "D"):
            self.moveDown()
        elif (direction == "L"):
            self.moveLeft()
        elif (direction == "R"):
            self.moveRight()
        return self

    def getHash(self): # returns the hash key for the board state, does not consider other factors like path 
        h = ""
        for i in self.board:
            h += str(i) + " "
        return hash(h)

    def getDepth(self): # returns the depth by counting the length of the path taken thus far
        return len(self.path)

    def getMisplacedTiles(self): # counts the number of misplaced tiles
        cnt = 0
        for i in range(len(self.board)):
            if i+1 != self.board[i]:
                cnt += 1
        return cnt

    def getManhattanDistance(self): # counts the manhattan distance, finds the "correct" row and column and subtracts the current one.
        count = 0
        for i in range(len(self.board)):
            if (i != self.pos):
                correctRow = int((i)/3)+1
                correctCol = int(i%3)+1
                row = int((self.board[i]-1)/3)+1
                col = int((self.board[i]-1)%3)+1
                count += abs(correctRow-row)
                count += abs(correctCol-col)
        return count

    def getMisplacedTilesHeuristic(self): # adds to cost to get value for a-star
        return int(self.getMisplacedTiles() + self.getDepth())
    
    def getManhattanHeuristic(self): # adds to cost to get value for a-star
        return int(self.getManhattanDistance() + (self.getDepth()*2))

