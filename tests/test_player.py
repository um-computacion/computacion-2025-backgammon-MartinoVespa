import unittest

class Backgammon:
    def __init__(self):
        self.myBoard = [0] * 24
        self.board = self.myBoard
        self.xJail = 0
        self.oJail = 0
        self.oHome = 15
        self.oFree = 0
        self.xHome = 15

class TestBackgammonMakeMove(unittest.TestCase):
    
    def test_wrong_side_or_empty_space(self):
        g = Backgammon()
        g.myBoard[7] = 0
        res = g.makeMove(space=7, side=False, steps=3)
        self.assertEqual(res, (False, "El espacio esta vacio o el equipo no es el correcto"))
