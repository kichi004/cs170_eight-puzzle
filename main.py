import py_compile

from slider import Slider
from search import Search, UniformSearch, ManhattanSearch, MisplacedSearch

list = [8, 7, 1, 6, 9, 2, 5, 4, 3]

x = Slider(list)

searcher = Search(x)
searcher.__class__ = ManhattanSearch

y = searcher.search()
searcher.followSolution(y.getPath())

