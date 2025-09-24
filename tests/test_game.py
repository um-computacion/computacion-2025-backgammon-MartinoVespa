import unittest

from core.game

class TestBackgammonMakeMove(unittest.TestCase):

    def test_jail_blocked_when_trying_to_move_with_steps(self):
        g = Backgammon()
        g.xJail = 1
        result = g.makeMove(space=5, side=True, steps=2)
        self.assertEqual(result, (False, "Asegurate primero de liberar tu ficha de la carcel"))

 def test_move_and_capture_sends_to_jail(self):

        g = Backgammon()
        g.myBoard[5] = 2 
        g.myBoard[6] = -1  
        res = g.makeMove(space=5, side=False, steps=1)
        self.assertEqual(res, (True, "Enviar a uno a la carcel"))
        self.assertEqual(g.myBoard[5], 1)   
        self.assertEqual(g.myBoard[6], 1)   
        self.assertEqual(g.xJail, 1) 
        