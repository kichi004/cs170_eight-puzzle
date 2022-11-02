import py_compile
import time

from slider import Slider
from search import GeneralSearch, UniformSearch, ManhattanSearch, MisplacedSearch

def eightPuzzleSolver():
    puzzleSelection = input("\nWelcome to my Eight Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own: ")
    if puzzleSelection == "1":
        listIm = [1, 2, 3, 4, 5, 6, 8, 7, 9]
        list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 = [1, 2, 3, 4, 5, 6, 9, 7, 8]
        list4 = [1, 2, 3, 5, 9, 6, 4, 7, 8]
        list8 = [1, 3, 6, 5, 9, 2, 4, 7, 8]
        list12 = [1, 3, 6, 5, 9, 7, 4, 8, 2]
        list16 = [1, 6, 7, 5, 9, 3, 4, 8, 2]
        list20 = [7, 1, 2, 4, 8, 5, 6, 3, 9]
        list = [9, 7, 2, 4, 6, 1, 3, 5, 8]
    else:
        list = []
        print("\nEnter your puzzle, using the highest value integer to represent the blank. Please only enter valid 8-Puzzles. Enter the puzzle delimiting the numbers with a space. Type RETURN only when finished.")
        firstRow = input("Enter the first row: ")
        insertRow(list, firstRow)
        secondRow = input("Enter the second row: ")
        insertRow(list, secondRow)
        thirdRow = input("Enter the third row: ")
        insertRow(list, thirdRow)
        # add additional rows if you want to solve 16- or 25- puzzles.
        '''
        fourthRow = input("Enter the fourth row: ")
        insertRow(list, fourthRow)
        '''
    x = Slider(list)

    searcher = GeneralSearch(x)
    algorithmSelection = input("\nSelect an algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic: ")
    if algorithmSelection == "1":
        searcher.__class__ = UniformSearch
    elif algorithmSelection == "2":
        searcher.__class__ = MisplacedSearch
    else:
        searcher.__class__ = ManhattanSearch

    print("\nSearching...")
    start = time.perf_counter()
    y = searcher.search()
    stop = time.perf_counter()
    if y.isCorrect():
        searcher.followSolution(y.getPath())
    print("Search took " + str(round(stop-start, 2)) + " seconds to run.\n")

def insertRow(list, row):
    input = row
    while (len(input)!=0):
        input = input.strip(" ")
        if (len(input) > 1):
            list.append(int(str(input[0]+input[1]))) # included to support 2-digit values
        else:
            list.append(int(input[0]))
        input = input[2:]

eightPuzzleSolver()