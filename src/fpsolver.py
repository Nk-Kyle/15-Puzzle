import heapq
from node import *
from copy import deepcopy
from heapq import *
from puzzle import *
directions = {'R' : [0,1], 'L' : [0,-1], 'D' : [1,0], 'U' : [-1,0]}
nodes = []
goalState = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
hashes = {}
isFound = False
comparisons = 0
resultNode : Node

def hashState(mat):
    idx = 0
    for i in range(16):
        row = i // 4
        col = i %4
        val = mat[row][col]
        idx |= i << (val * 4)
    return idx
    
hashgoal = hashState(goalState)

def solve(mat):
    global resultNode
    global hashes
    global isFound
    global comparisons
    global nodes
    nodes = []
    comparisons = 0
    isFound = False
    hashes = {}
    x,y = findBlank(mat)
    newNode = Node(mat,None,0,None,[x,y])
    heappush(nodes,newNode )
    if(hashState(mat) != hashgoal):
        while(len(nodes) > 0):
            if(isFound):
                #Bound any further search if goal is found and head of priority worse than resultNode
                if(nodes[0].c >= resultNode.c):
                    break
            evalNode = heappop(nodes)
            evalChilds(evalNode)
        path = getPath(resultNode)
    else:
        path = [newNode]

    return path, comparisons

def getPath(CurNode):
    path = []
    while(CurNode.parent != None):
        path.append(CurNode)
        CurNode = CurNode.parent
    path.append(CurNode)
    return path

def findBlank(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 16):
                return i,j

def evalChilds(curnode):
    global hashes
    global resultNode
    global isFound
    global comparisons
    for dir in directions:
        if (validMove(curnode,dir)):
            newMat = swap(curnode,dir)
            # hashstates to avoid duplicates
            hashval = hashState(newMat)
            if(hashval == hashgoal):
                isFound = True
                resultNode = Node(newMat, curnode, curnode.f + 1, dir,[curnode.blank[0] + directions[dir][0], curnode.blank[1] + directions[dir][1]])
                comparisons +=1
                break
            elif(hashval not in hashes):
                hashes[hashval] = True
                comparisons += 1
                newNode = Node(newMat, curnode, curnode.f + 1, dir,[curnode.blank[0] + directions[dir][0], curnode.blank[1] + directions[dir][1]])
                heappush(nodes,newNode )
    return

def validMove(curnode : Node, dir):
    newblankpos = [curnode.blank[0] + directions[dir][0], curnode.blank[1] + directions[dir][1]]
    return (newblankpos[0] in range(0,4) and newblankpos[1] in range(0,4))

def swap(curnode: Node, dir):
    newmat = deepcopy(curnode.state)
    x = curnode.blank[0]
    y = curnode.blank[1]
    newx = x + directions[dir][0]
    newy = y + directions[dir][1]
    newmat[x][y] = newmat[newx][newy]
    newmat[newx][newy] = 16
    return newmat



def solvable(mat):
    kurang,blankidx = countKurang(mat)
    tot = 0
    for row in mat:
        for col in row:
            tot += kurang[col-1]
    issolvable = ((blankidx + tot) % 2 == 0)
    return kurang, tot, blankidx, issolvable

def countKurang(mat):
    kurang = [0 for i in range(16)]
    for i in range(16):
        row = i // 4
        col = i % 4
        refer = mat[row][col]
        if (refer == 16):
            blankidx = row+col
        for j in range(i,16):
            row = j // 4
            col = j % 4
            check = mat[row][col]
            if (check < refer):
                kurang[refer-1] += 1
    return kurang, blankidx