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