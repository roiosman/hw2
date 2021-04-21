import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5

    def get_animal(self):
        sca = [" "] * 5
        for i in range(len(sca)):
            sca[i] = [" "] * 8
        for i in range(0, 6):
            for j in range(0, 8):
                if (i == 0):
                    if (j ==0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
                        sca[i][j] = "*"
                elif (i == 1):
                    if ( j == 4 or j== 5 or j == 6):
                        sca[i][j] = "*"
                elif (i == 2):
                    if (j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 7):
                        sca[i][j] = "*"
                elif (i == 3):
                    if ( j == 4 or j== 5 or j == 6):
                        sca[i][j] = "*"
                if (i == 4):
                    if (j ==0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
                        sca[i][j] = "*"
        if (self.directionH == 1):
            return sca
        else:
            for i in range(len(sca)):
                sca[i].reverse()
            return sca