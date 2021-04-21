import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 3

    def get_animal(self):
        mol = [" "] * 3
        for i in range(len(mol)):
            mol[i] = [" "] * 8
        for i in range(0, 4):
            for j in range(0, 8):
                if (i == 0):
                    if (j == 1 or j == 2 or j == 3 or j ==4 or j == 7):
                        mol[i][j] = "*"
                elif (i == 1):
                    mol[i][j] = "*"
                elif (i == 2):
                    if (j == 1 or j == 2 or j == 3 or j == 4 or j == 7):
                        mol[i][j] = "*"
        if (self.directionH == 0):
            return mol
        else:
            for i in range(len(mol)):
                mol[i].reverse()
            return mol