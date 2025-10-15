class board:
    def __init__(self):
        self.myboard = {}
        for i in range(24):
            self.myboard[i] = 0
        self.myboard[0] = 2
        self.myboard[5] = -5
        self.myboard[7] = -3
        self.myboard[11] = 5
        self.myboard[12] = -5
        self.myboard[16] = 3
        self.myboard[18] = 5
        self.myboard[23] = -2
        self.maxRows = 5
        self.xFree = 0
        self.oFree = 0
        self.xJail = 0
        self.oJail = 0
        self.xHome = 5
        self.oHome = 5

def makeMove(self, space, side, steps):
    if side:
        if (self.xJail > 0 and (steps != 0 or space < 18)):
            return (False, "Hacegurate de que la pieza este fuera de la carcel primero")
        elif (self.xJail > 0 and steps == 0 and space > 17):
            if (self.myBoard[space] > 1):
                return (False, "El espacio esta ocupado")
            elif (self.myBoard[space] == 1):
                self.xJail = self.xJail - 1
                self.myBoard[space] = -1
                self.oJail = self.oJail + 1
                self.oHome = self.oHome - 1
                return (True, "Pieza liberada de la carcel y envio a otra a la carcel")
            else:
                self.xJail = self.xJail - 1
                self.myBoard[space] = self.myBoard[space] - 1
                return (True, "Pieza liberada de la carcel")
        elif (self.myBoard[space] >= 0):
            return (False, "El espacio se enuentra vacio o el equipo es el incorrecto")
        else:
            newSpace = space - steps
            if (newSpace < 0):
                if (self.xHome < 15):
                    return (False, "Asegurate de que todas tus piezas esten en tu casa antes de sacarlas afuera")
                else:
                    self.myBoard[space] = self.myBoard[space] - 1
                    self.xFree = self.xFree + 1
                    return (True, "Pieza despejada")
            elif (self.myBoard[newSpace] > 1):
                return (False, "Nuevo espacio ocupado")
            elif (self.myBoard[newSpace] == 1):
                self.myBoard[space] = self.myBoard[space] + 1
                self.myBoard[newSpace] = -1
                self.oJail = self.oJail + 1
                if (newSpace >= 18):
                    self.oHome = self.oHome - 1
                return (True, "Se envio a uno a la carcel")
            