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
        