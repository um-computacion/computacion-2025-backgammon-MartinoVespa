import unittest

from core import board

class Backgammon:
    def __init__(self):
        self.myBoard = [0] * 24
        self.board = self.myBoard
        self.xJail = 0
        self.oJail = 0
        self.oHome = 15
        self.oFree = 0
        self.xHome = 15

def makeMove(self, space, side, steps):

        if side:
            if self.xJail > 0 and (steps != 0 or space < 18):
                return (False, "Asegurate primero de liberar tu ficha de la carcel")
            elif (self.xJail > 0 and steps == 0 and space > 17):
                if (self.myBoard[space] > 1):
                    return (False,"Ese lugar ya está ocupado")
                elif (self.xJail > 0 and steps == 0 and space > 17):
                    if (self.myBoard[space] > 1):
                        return (False, "El espacio esta ocupado")
                    elif (self.myBoard[space] == 1):
                        self.xJail = self.xJail - 1
                        self.myBoard[space] = -1
                        self.oJail = self.oJail + 1
                        self.oHome = self.oHome - 1
                        return (True, "Una pieza salio de la carcel y envio a otra a la carcel")
                    else:
                        self.xJail = self.xJail - 1
                        self.myBoard[space] = self.myBoard[space] - 1
                        return (False, )
                else:
                        self.oJail -= 1
                        self.myBoard[space] = 1
                        return (True, "Una pieza salió de la carcel y se movió al espacio vacío")

            else:
                self.oJail = self.oJail - 1
                self.myBoard[space] = self.myBoard[space] + 1
                return (True, "La pieza salio de la carcel")
        elif (self.myBoard[space] <= 0):
            return (False, "El espacio esta vacio o el equipo no es el correcto")
        else:
            newSpace = space + steps
            if (newSpace > 23):
                if (self.oHome < 15):
                    return (False, "Asegurate que todas tus piezas esten en tu base antes de sacarlas")
                else:
                    self.myBoard[space] = self.myBoard[space] - 1
                    self.oFree = self.oFree + 1
                    return (True, "Pieza despejada")
            elif (self.myBoard[newSpace] < -1):
                return (False, "El nuevo espacio esta ocupado")
            elif (self.myBoard[newSpace] == -1):
                self.myBoard[space] = self.myBoard[space] - 1
                self.myBoard[newSpace] = 1
                self.xJail = self.xJail + 1
                if (newSpace < 6):
                    self.xHome = self.xHome - 1
                return (True, "Enviar a uno a la carcel")
            else:
                self.myBoard[space] = self.myBoard[space] - 1
                self.myBoard[newSpace] = self.myBoard[newSpace] + 1
                if (newSpace > 17):
                    self.oHome = self.oHome + 1
                if (newSpace > 11):
                    self.updateRows(True)
                else:
                    self.updateRows(False)
                return (True, "Movimiento hecho")
            
def updateRows(self, top):
        changed = False
        if top:
            for i in range(12):
                point = self.board[i]
                if self.updatePoint(i, point):
                    changed = True
        else:
            for i in range(12, 24):
                point = self.board[i]
                if self.updatePoint(i, point):
                    changed = True
        return changed

def test_repr_contains_labels():
        b = board()
        text = repr(b)
        assert "X TABLERO DE INICIO" in text
        assert "O TABLERO DE INICIO" in text

def test_populateTop_and_populateBottom():
     b = board()
     top = b.populateTop(0)
     bottom = b.populateBottom(0)
     assert "|" in top
     assert "|" in bottom

def test_wrong_side_or_empty_space(self):
        g = Backgammon()
        g.myBoard[7] = 0
        res = g.makeMove(space=7, side=False, steps=3)
        self.assertEqual(res, (False, "El espacio esta vacio o el equipo no es el correcto"))

        