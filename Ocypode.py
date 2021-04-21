import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        super().__init__(name, age, x, y, directionH)
        self.width = 7
        self.height = 4

    def get_animal(self):
        ocy = [" "]*4
        for i in range (len(ocy)):
            ocy[i] = [" "] * 7
        for i in range(0, 5):
            for j in range(0, 7):
                if (i == 0):
                    if (j == 1 or j == 5):
                        ocy[i][j] = "*"
                elif (i == 1):
                    if (j == 2 or j == 3 or j == 4):
                        ocy[i][j] = "*"
                elif (i == 2):
                    ocy[i][j] = "*"
                elif (i == 3):
                    if (j == 0 or j == 6):
                        ocy[i][j] = "*"
        if(self.directionH == 0):
            return ocy
        else:
            for i in range (len(ocy)):
                ocy[i].reverse()
            return ocy
