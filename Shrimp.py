import Crab


class Shrimp(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 3

    def get_animal(self):
        shr = [" "] * 3
        for i in range(len(shr)):
            shr[i] = [" "] * 7
        for i in range(0, 4):
            for j in range(0, 7):
                if (i == 0):
                    if (j == 0 or j == 3):
                        shr[i][j] = "*"
                elif (i == 1):
                    if (j != 0):
                        shr[i][j] = "*"
                elif (i == 2):
                    if (j == 2 or j == 4):
                        shr[i][j] = "*"
        if (self.directionH == 0):
            return shr
        else:
            for i in range(len(shr)):
                shr[i].reverse()
            return shr