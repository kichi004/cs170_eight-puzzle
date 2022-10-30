import py_compile

from slider import Slider
from search import Search, UniformSearch, ManhattanSearch, MisplacedSearch

def eightPuzzleSolver():
    selection = input("\nWelcome to my Eight Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own: ")
    if selection == "1":
        list = [8, 7, 1, 6, 9, 2, 5, 4, 3]
    else:
        list = []
        print("\nEnter your puzzle, using the highest value integer to represent the blank. Please only enter valid 8-Puzzles. Enter the puzzle demilimiting the number with a space. Type RETURN only when finished.")
        firstRow = input("Enter the first row: ")
        rowInput(list, firstRow)
        secondRow = input("Enter the second row: ")
        rowInput(list, secondRow)
        thirdRow = input("Enter the third row: ")
        rowInput(list, thirdRow)
    x = Slider(list)

    searcher = Search(x)
    algorithm = input("\nSelect an algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, or (3) for the Manhattan Distance Heuristic: ")
    if algorithm == "2":
        searcher.__class__ = MisplacedSearch
    elif algorithm == "3":
        searcher.__class__ = ManhattanSearch
    else:
        searcher.__class__ = UniformSearch

    print("\nSearching...")
    y = searcher.search()
    searcher.followSolution(y.getPath())


def rowInput(list, row):
    input = row
    while (len(input)!=0):
        input = input.lstrip(" ")
        list.append(int(input[0]))
        input = input[1:]
    

eightPuzzleSolver()