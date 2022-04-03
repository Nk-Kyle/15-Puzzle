import heapq
from time import sleep
from node import *
from copy import deepcopy
from heapq import *
from puzzle import *
directions = {'U' : [0,1], 'D' : [0,-1], 'R' : [1,0], 'L' : [-1,0]}
nodes = []
goalState = [[2,1,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
hashes = []
isFound = False

def solve(mat):
    x,y = findBlank(mat)
    newNode = Node(mat,None,0,None,[x,y])
    heappush(nodes,newNode )
    while(len(nodes) > 0):
        if(isFound):
            if(nodes[0].c() > resultNode.c()):
                break
        if (isFound):
            print(isFound)
        evalNode = heappop(nodes)
        evalChilds(evalNode)
    return resultNode

def findBlank(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 16):
                return i,j

def evalChilds(curnode):
    global hashes
    for dir in directions:
        if (validMove(curnode,dir)):
            newMat = swap(curnode,dir)
            hashval = hash(newMat)
            if(hashval == hash(goalState)):
                global resultNode
                global isFound
                isFound = True
                resultNode = Node(newMat, curnode, curnode.f + 1, dir,[x + y for x,y in zip(curnode.blank, directions[dir])])
            elif(hashval not in hashes):
                hashes.append(hashval)
                newNode = Node(newMat, curnode, curnode.f + 1, dir,[x + y for x,y in zip(curnode.blank, directions[dir])])
                print(newNode.c)
                heappush(nodes,newNode )

def validMove(curnode : Node, dir):
    try:
        testdir = [x + y for x,y in zip(directions[curnode.dir], directions[dir])]
    except:
        testdir = directions[dir]
    if (testdir[0] == 0 and testdir[1] == 0):
        return False
    else:
        newblankpos = [x + y for x,y in zip(curnode.blank, directions[dir])]
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

def hash(mat):
    idx = 0
    for i in range(16):
        row = i // 4
        col = i %4
        val = mat[row][col]
        idx |= i << (val * 4)
    return idx

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