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
                temp += self.hamdist(refer,i,j)
        return temp

    def hamdist(self,val, i, j):
        row = val//4
        col = val%4
        return(abs(row-i) + abs(col-i))
    def __lt__(self, other):
        return self.c < other.c