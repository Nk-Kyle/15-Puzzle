class Node(object):
    def __init__(self, state, parent, f, dir, blankpos):
        self.state = state
        self.parent = parent
        self.f = f
        self.g = self.calcg()
        self.c = f + self.g
        self.dir = dir
        self.blank = blankpos

    def calcg(self):
        temp =0
        for i in range(4):
            for j in range(4):
                refer = self.state[i][j]
                if (refer != 16 and i*4+j+1 != refer):
                    temp += 1
        return temp

    def __lt__(self, other):
        return self.c < other.c