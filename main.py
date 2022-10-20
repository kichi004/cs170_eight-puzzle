import array as arr

class Slider:
    def __init__(self):
        self.a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])    # array representing the game board, 9 = blank
        self.l = 3  # side length of the array
        self.p = 8  # position of the blank
        self.path = ""  # string to track previous actions taken


