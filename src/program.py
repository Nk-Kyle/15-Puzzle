from cgitb import enable
from tkinter import *
from tkinter import messagebox
from puzzle import *
from fpsolver import *
from time import time
root = Tk()
root.title("15 Puzzle")

path = []
idx = 0

def showprev():
    global idx
    if (idx == 1):
        leftbutton['state'] = DISABLED
    rightbutton['state'] = NORMAL
    idx -= 1
    setEntries(path[idx].state)
    

def shownext():
    global idx
    if (idx == len(path) - 2):
        rightbutton['state'] = DISABLED
    leftbutton["state"] = NORMAL
    idx += 1
    setEntries(path[idx].state)

def disableEntries():
    for e in grids:
        e.config(state=DISABLED)

def enableEntries():
    for e in grids:
        e.config(state=NORMAL)

def help():
    messagebox.showinfo("Help","Enter number 1-15 in the grid or press random to generate a random puzzle.\n\nPress solve to solve the puzzle.\n\nPress reset to reset the puzzle.\n\nUse arrow to navigate the puzzle.")

def randomize():
    mat = random()
    setEntries(mat)

def getEntries():
    mat = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mat[i][j] = getVal(entries[i][j])
    return mat

def getVal(entry):
    if(entry.get() == ''):
        return 16
    return int(entry.get())
def solvePuzzle():
    try:
        global path
        disableEntries()
        solvebutton['state'] = DISABLED
        randombutton['state'] = DISABLED
        mat = getEntries()
        validate(mat)
        begin = time()
        (path, built) = solve(mat)
        end = time()
        path.reverse()
        timeVal.set( str(end-begin) + ' ms')
        nodesVal.set( str(built))
        if(len(path) > 1):
            rightbutton['state'] = NORMAL
    except:
        enableEntries()
        messagebox.showerror("Error","Invalid input")
        solvebutton['state'] = NORMAL
        randombutton['state'] = NORMAL

def reset():
    setEntries([[i*4+j+1 for j in range(4)] for i in range(4)])
    enableEntries()
    timeVal.set('')
    nodesVal.set('')
    solvebutton['state'] = NORMAL
    randombutton['state'] = NORMAL
    return

def setEntries(mat):
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 16):
                mat[i][j] = ''
    for i in range(4):
        for j in range(4):
            entry = entries[i][j]
            entry.set(mat[i][j])


   
mainlabel = Label(root, text="Configuration", font=("Helvetica", 10),justify=CENTER)
mainlabel.grid(row=0, column=0, columnspan=3)

#Time Label
timelable = Label(root, text="Time", font=("Helvetica", 10),justify=CENTER)
timelable.grid(row=3, column=4)
timeVal = StringVar()
timeVallabel = Label(root, textvariable=timeVal, font=("Helvetica", 10),justify=CENTER)
timeVallabel.grid(row=3, column=5)

#Nodes Created Label
nodeslabel = Label(root, text="Nodes Created", font=("Helvetica", 10),justify=CENTER)
nodeslabel.grid(row=4, column=4)
nodesVal = StringVar()
nodesVallabel = Label(root, textvariable=nodesVal, font=("Helvetica", 10),justify=CENTER)
nodesVallabel.grid(row=4, column=5)

helpbutton = Button(root, text="Help", command=help)
helpbutton.grid(row=0, column=3)

leftbutton = Button(root, text="<", command=showprev, width=3, state=DISABLED)
leftbutton.grid(row=5, column=0)
resetbutton = Button(root, text="Reset", command=reset, width=10)
resetbutton.grid(row=5, column=1,columnspan=2)
rightbutton = Button(root, text=">", command=shownext, width=3, state=DISABLED)
rightbutton.grid(row=5, column=3)
randombutton = Button(root, text="Random", command=randomize, height=2, width = 12)
randombutton.grid(row=0, column=4, rowspan=2)
solvebutton = Button(root, text="Solve", command=solvePuzzle, height=2, width = 12)
solvebutton.grid(row=1, column=4, rowspan=2)

#set StringVar for each entry
entry1 = StringVar()
entry2 = StringVar()
entry3 = StringVar()
entry4 = StringVar()
entry5 = StringVar()
entry6 = StringVar()
entry7 = StringVar()
entry8 = StringVar()
entry9 = StringVar()
entry10 = StringVar()
entry11 = StringVar()
entry12 = StringVar()
entry13 = StringVar()
entry14 = StringVar()
entry15 = StringVar()
entry16 = StringVar()
entries = [[entry1,entry2,entry3,entry4],[entry5,entry6,entry7,entry8],[entry9,entry10,entry11,entry12],[entry13,entry14,entry15,entry16]]

#Create Grid of 3x3 aligned center, filled 1-15
e1 = Entry(root, width=5,borderwidth= 5, justify=CENTER, textvariable= entry1)
e1.grid(column=0, row=1,  ipady= 5)
e2 = Entry(root, width=5, borderwidth= 5, justify=CENTER, textvariable= entry2)
e2.grid(column=1, row=1, ipady= 5)
e3 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry3)
e3.grid(column=2, row=1, ipady= 5)
e4 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry4)
e4.grid(column=3, row=1, ipady= 5)

e5 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry5)
e5.grid(column=0, row=2, ipady= 5)
e6 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry6)
e6.grid(column=1, row=2, ipady= 5)
e7 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry7)
e7.grid(column=2, row=2, ipady= 5)
e8 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry8)
e8.grid(column=3, row=2, ipady= 5)

e9 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry9)
e9.grid(column=0, row=3, ipady= 5)
e10 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry10)
e10.grid(column=1, row=3, ipady= 5)
e11 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry11)
e11.grid(column=2, row=3, ipady= 5)
e12 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry12)
e12.grid(column=3, row=3, ipady= 5)

e13 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry13)
e13.grid(column=0, row=4, ipady= 5)
e14 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry14)
e14.grid(column=1, row=4, ipady= 5)
e15 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry15)
e15.grid(column=2, row=4, ipady= 5)
e16 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry16)
e16.grid(column=3, row=4, ipady= 5)

grids = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
# Set each grid to numbers 1-15 and blank
setEntries([[i*4+j+1 for j in range(4)] for i in range(4)])
root.mainloop()