import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []
        global anim_list
        anim_list = self.anim


    def build_tank(self):
        for i in range(len(self.board)):
            self.board[i] = [' '] * self.aqua_width
        for i in range(self.aqua_height - 1):
            self.board[i][0] = "|"
            self.board[i][self.aqua_width - 1] = "|"
        self.board[self.aqua_height - 1][0] = '\\'
        self.board[self.aqua_height - 1][self.aqua_width - 1] = '/'
        for i in range(1, self.aqua_width - 1):
            self.board[2][i] = "~"
            self.board[self.aqua_height - 1][i] = "_"

    def print_board(self):
        for x in self.board:
            print (*x)

    def get_board(self):
        return self.board

    def get_all_animal(self):
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        pass
        if (animal.directionH == 1):
            checka = animal.x + animal.width
        else:
            checka = animal.x - 1
        for z in self.anim:
            if (isinstance(z, Crab.Crab) and z != animal):
                if(animal.directionH == z.directionH):
                    continue
                if (z.directionH == 1):
                    checkb = z.x + z.width
                else:
                    checkb = z.x - 1
                print(checka)
                print(checkb)
                if (z.directionH == 1 and animal.directionH == 0 and isinstance(z, Ocypode.Ocypode) and isinstance(animal, Shrimp.Shrimp) and checka == checkb):
                    return False
                elif (z.directionH == 0 and animal.directionH == 1 and isinstance(z, Shrimp.Shrimp) and isinstance(animal, Ocypode.Ocypode) and checka == checkb):
                    return False
                else:
                    if(animal.directionH == 1 and z.directionH == 0):
                        return (checka == checkb or (checka-1) == checkb)
                    else:
                        return (checka == checkb or (checkb - 1) == checka)



    def print_animal_on_board(self, animal: Animal):
        if (isinstance(animal,Ocypode.Ocypode)):
            for i in range(self.aqua_height - 5, self.aqua_height - 1):
                for j in range(animal.x, animal.x + 7):
                    if(animal.get_animal()[i-(self.aqua_height - 5)][j-animal.x] == "*"):
                        self.board[i][j] = animal.get_animal()[i-(self.aqua_height - 5)][j-animal.x]
        elif (isinstance(animal, Shrimp.Shrimp)):
            for i in range(self.aqua_height - 4, self.aqua_height - 1):
                for j in range(animal.x, animal.x + 7):
                    if(animal.get_animal()[i-(self.aqua_height - 4)][j-animal.x] == "*"):
                        self.board[i][j] = animal.get_animal()[i-(self.aqua_height - 4)][j-animal.x]
        elif (isinstance(animal, Moly.Moly)):
            for i in range(animal.y, animal.y + 3):
                for j in range(animal.x, animal.x + 8):
                    if(animal.get_animal()[i-animal.y][j-animal.x] == "*"):
                        self.board[i][j] = animal.get_animal()[i-animal.y][j-animal.x]
        elif (isinstance(animal, Scalar.Scalar)):
            for i in range(animal.y, animal.y +5):
                for j in range(animal.x, animal.x + 8):
                    if(animal.get_animal()[i - animal.y][j - animal.x] == "*"):
                        self.board[i][j] = animal.get_animal()[i - animal.y][j - animal.x]


    def delete_animal_from_board(self, animal: Animal):
        self.anime.remove(animal)

    def add_fish(self, name, age, x, y, directionH, directionV, fishtype):
        if (fishtype == "sc"):
            f = Scalar.Scalar(name, age, x, y ,directionH, directionV)
        else:
            f = Moly.Moly(name, age, x, y, directionH, directionV)
        if (f.x +f.width > self.aqua_width-1):
            f.x = self.aqua_width -1 -f.width
        if (f.y + f.height > self.aqua_height - 5):
            f.y = self.aqua_height-5-f.height
        for s in self.anim:
            if(isinstance(s, Fish.Fish)):
                for i in range(f.height):
                    for j in range (f.width):
                        if ( s.y <= f.y + i and f.y + i <= s.y+s.height and s.x <= f.x+j and f.x + j <= s.x +s.width):
                            return False
        self.anim.append(f)
        return True



    def add_crab(self, name, age, x, y, directionH, crabtype):
        if (crabtype == "sh"):
            c = Shrimp.Shrimp(name, age, x, y ,directionH)
        else:
            c = Ocypode.Ocypode(name, age, x, y, directionH)
        if (c.x +c.width > self.aqua_width-1):
            c.x = self.aqua_width - 1 - c.width
        for s in self.anim:
            if (isinstance(s, Crab.Crab)):
                for i in range(c.height):
                    for j in range(c.width):
                        if (s.x <= c.x + j and c.x + j <= s.x + s.width):
                            return False
        self.anim.append(c)
        return True

    def check_if_free(self, x, y) -> bool:
        if (self.board[y][x] != " "):
            return False
        return True

    def left(self, a):
        a.x = a.x -1

    def right(self, a):
        a.x = a.x +1

    def up(self, a):
        a.y = a.y +1

    def down(self, a):
        a.y = a.y -1

    def next_turn(self):
        if(self.turn % 10 ==0):
            for i in self.anim:
                i.food = i.food - 1
                if (self.turn % 100 ==0):
                    i.age = i.age + 1
        kill = []
        for i in self.anim:
            print(i.food)
            if(not i.get_alive()):
                i.die()
                kill.append(i)
        self.anim = [i for i in self.anim if i not in kill]
        collideh = []
        collidev = []
        collidec = []
        for i in self.anim:
            if(i.directionH == 0 and i.x == 1):
                i.directionH = 1
                if(i not in collideh):
                    collideh.append(i)
            if (i.directionH == 1 and i.x + i.width == self.aqua_width-1):
                i.directionH = 0
                if (i not in collideh):
                    collideh.append(i)
            if(isinstance(i, Fish.Fish)):
                if (i.directionV == 1 and i.y == 3):
                    i.directionV = 0
                    if (i not in collidev):
                        collidev.append(i)
                if (i.directionV == 0 and i.y + i.height == self.aqua_height - 5):
                    i.directionV = 1
                    if (i not in collidev):
                        collidev.append(i)
            if (isinstance(i,Crab.Crab)):
                bol = self.is_collision(i)
                print (str(bol))
                if (bol):
                    if (i not in collidec):
                        collidec.append(i)
        for i in self.anim:
            if (isinstance(i, Fish.Fish)):
                if(i not in collideh):
                    if (i.directionH == 0):
                        i.x = i.x - 1
                    else:
                        i.x = i.x + 1
                if(i not in collidev):
                    if (i.directionV == 0):
                        i.y = i.y + 1
                    else:
                        i.y = i.y - 1
                else:
                    if(i in collideh):
                        i.directionH = (i.directionH + 1) % 2
                    elif(i in collidec):
                        i.directionH = (i.directionH + 1) % 2
                        if (i.directionH == 0):
                            i.x = i.x - 1
                        else:
                            i.x = i.x + 1
                    else:
                        if (i.directionH == 0):
                            i.x = i.x - 1
                        else:
                            i.x = i.x + 1
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.turn += 1

    def print_all(self):
        for i in self.anim:
            print(i.__str__())

    def feed_all(self):
        for i in self.anim:
            i.food = i.food + 10

    def add_animal(self, name, age, x, y, directionH, directionV, animaltype):
        if animaltype == 'sc' or animaltype == 'mo':
             return self.add_fish(name, age, x, y, directionH, directionV, animaltype)
        elif animaltype == 'oc' or animaltype == 'sh':
             return self.add_crab(name, age, x, y, directionH, animaltype)
        else:
            return False

    def several_steps(self) -> None:
        several = int(input("How many steps would you want to take?"))
        while (several > 0):
            self.next_turn()
            for i in self.anim:
                self.print_animal_on_board(i)
            self.print_board()
            several = several -1


