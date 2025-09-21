import unittest

from core.game

class TestBackgammonMakeMove(unittest.TestCase):

    def test_jail_blocked_when_trying_to_move_with_steps(self):
        g = Backgammon()
        g.xJail = 1
        result = g.makeMove(space=5, side=True, steps=2)
        self.assertEqual(result, (False, "Asegurate primero de liberar tu ficha de la carcel"))
        