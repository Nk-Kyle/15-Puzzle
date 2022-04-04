from cgitb import enable
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
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
    navVal.set('Puzzle Solved\nSteps:\n' + str(idx) + '/' + str(len(path)-1))

def shownext():
    global idx
    if (idx == len(path) - 2):
        rightbutton['state'] = DISABLED
    leftbutton["state"] = NORMAL
    idx += 1
    setEntries(path[idx].state)
    navVal.set('Puzzle Solved\nSteps:\n' + str(idx) + '/' + str(len(path)-1))

def disableEntries():
    for e in grids:
        e.config(state=DISABLED)

def enableEntries():
    for e in grids:
        e.config(state=NORMAL)

def openfile():
    filepath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    try:
        mat = read(filepath)
        setEntries(mat)
    except:
        messagebox.showerror("Error","Invalid input")
        return
def help():
    messagebox.showinfo("Help","Enter number 1-15 in the grid or press random to generate a random puzzle.\n\nPress solve to solve the puzzle.\n\nPress Open File to use configuration from existing file\n\nPress reset to reset the puzzle.\n\nUse arrow to navigate the puzzle.")

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

def setKurang():
    for i in range(4):
        for j in range(4):
            kurangval = kurang[i*4+j]
            kurangString = kuranglist[i][j]
            kurangString.set('KURANG('+str(i*4+j+1) + ') = ' + str(kurangval))
    kuranghead.set('Nilai KURANG(i)')
    kurangstat.set('\u03a3(Kurang(i)) + X = ' + str(tot)+ ' + '+ str(blankidx%2) +' = ' + str(tot+(blankidx%2)))

def solvePuzzle():
    try:
        global path
        global idx
        global kurang, tot, blankidx, issolveable
        idx = 0
        mat = getEntries()
        kurang,tot, blankidx, issolveable = solvable(mat)
        setKurang()
        validate(mat)
        disableEntries()
        solvebutton['state'] = DISABLED
        randombutton['state'] = DISABLED
        openfilebutton['state'] = DISABLED
    except:
        enableEntries()
        messagebox.showerror("Error","Invalid input")
        solvebutton['state'] = NORMAL
        randombutton['state'] = NORMAL
    
    if (issolveable):
        begin = time()
        (path, built) = solve(mat)
        end = time()
        path.reverse()
        timeVal.set( str(end-begin) + ' ms')
        nodesVal.set( str(built))
        if(len(path) > 1):
            rightbutton['state'] = NORMAL
        navVal.set('Puzzle Solved\nSteps:\n' + '0/' + str(len(path)-1))
    else:
        messagebox.showerror("Error","Configuration can't be solved")

def reset():
    setEntries([[i*4+j+1 for j in range(4)] for i in range(4)])
    enableEntries()
    timeVal.set('')
    nodesVal.set('')
    solvebutton['state'] = NORMAL
    randombutton['state'] = NORMAL
    openfilebutton['state'] = NORMAL
    leftbutton['state'] = DISABLED
    rightbutton['state'] = DISABLED
    for i in range(4):
        for j in range(4):
            kuranglist[i][j].set('')
    kuranghead.set('')
    kurangstat.set('')
    navVal.set('')

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

#Time Labels
timelable = Label(root, text="Time", font=("Helvetica", 10),justify=CENTER)
timelable.grid(row=4, column=4)
timeVal = StringVar()
timeVallabel = Label(root, textvariable=timeVal, font=("Helvetica", 10),justify=CENTER)
timeVallabel.grid(row=4, column=5)

#Nodes Created Label
nodeslabel = Label(root, text="Nodes Created", font=("Helvetica", 10),justify=CENTER)
nodeslabel.grid(row=5, column=4)
nodesVal = StringVar()
nodesVallabel = Label(root, textvariable=nodesVal, font=("Helvetica", 10),justify=CENTER)
nodesVallabel.grid(row=5, column=5)

#Kurang Labels
kuranghead = StringVar()
kurangheadlabel = Label(root, textvariable=kuranghead, font=("Helvetica", 10),justify=CENTER)
kurangheadlabel.grid(row=0, column=7, columnspan=2)
kurangstat = StringVar()
kurangstatlabel = Label(root, textvariable=kurangstat, font=("Helvetica", 10),justify=CENTER)
kurangstatlabel.grid(row=5, column=6, columnspan=4)

kurang1 = StringVar()
kurang1label = Label(root,textvariable= kurang1 , font=("Helvetica", 10),justify=CENTER)
kurang2 = StringVar()
kurang2label = Label(root,textvariable= kurang2 , font=("Helvetica", 10),justify=CENTER)
kurang3 = StringVar()
kurang3label = Label(root,textvariable= kurang3 , font=("Helvetica", 10),justify=CENTER)
kurang4 = StringVar()
kurang4label = Label(root,textvariable= kurang4 , font=("Helvetica", 10),justify=CENTER)

kurang5 = StringVar()
kurang5label = Label(root,textvariable= kurang5 , font=("Helvetica", 10),justify=CENTER)
kurang6 = StringVar()
kurang6label = Label(root,textvariable= kurang6 , font=("Helvetica", 10),justify=CENTER)
kurang7 = StringVar()
kurang7label = Label(root,textvariable= kurang7 , font=("Helvetica", 10),justify=CENTER)
kurang8 = StringVar()
kurang8label = Label(root,textvariable= kurang8 , font=("Helvetica", 10),justify=CENTER)

kurang9 = StringVar()
kurang9label = Label(root,textvariable= kurang9 , font=("Helvetica", 10),justify=CENTER)
kurang10 = StringVar()
kurang10label = Label(root,textvariable= kurang10 , font=("Helvetica", 10),justify=CENTER)
kurang11 = StringVar()
kurang11label = Label(root,textvariable= kurang11 , font=("Helvetica", 10),justify=CENTER)
kurang12 = StringVar()
kurang12label = Label(root,textvariable= kurang12 , font=("Helvetica", 10),justify=CENTER)

kurang13 = StringVar()
kurang13label = Label(root,textvariable= kurang13 , font=("Helvetica", 10),justify=CENTER)
kurang14 = StringVar()
kurang14label = Label(root,textvariable= kurang14 , font=("Helvetica", 10),justify=CENTER)
kurang15 = StringVar()
kurang15label = Label(root,textvariable= kurang15 , font=("Helvetica", 10),justify=CENTER)
kurang16 = StringVar()
kurang16label = Label(root,textvariable= kurang16 , font=("Helvetica", 10),justify=CENTER)

kuranglist = [[kurang1,kurang2,kurang3,kurang4],[kurang5,kurang6,kurang7,kurang8],[kurang9,kurang10,kurang11,kurang12],[kurang13,kurang14,kurang15,kurang16]]
kuranglabels = [[kurang1label, kurang2label, kurang3label, kurang4label],[kurang5label, kurang6label, kurang7label, kurang8label],[kurang9label, kurang10label, kurang11label, kurang12label],[kurang13label, kurang14label, kurang15label, kurang16label]]
# set grid for all kurang
for i in range(4):
    for j in range(4):
        kuranglist[i][j].set('')
        kuranglabels[i][j].grid(row=i+1, column=j+6)

#Navigation Label
navVal = StringVar()
navlabel = Label(root, textvariable=navVal, font=("Helvetica", 10),justify=CENTER)
navlabel.grid(row=6, column=0, columnspan=4)

#Buttons
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
openfilebutton = Button(root, text="Open File", command=openfile, height=2, width = 12)
openfilebutton.grid(row=2, column=4, rowspan=2)

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
e2 = Entry(root, width=5, borderwidth= 5, justify=CENTER, textvariable= entry2)
e3 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry3)
e4 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry4)

e5 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry5)
e6 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry6)
e7 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry7)
e8 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry8)

e9 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry9)
e10 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry10)
e11 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry11)
e12 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry12)

e13 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry13)
e14 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry14)
e15 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry15)
e16 = Entry(root, width=5, borderwidth= 5, justify=CENTER,textvariable= entry16)

grids = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16]
#set grid for all entry
for i in range(16):
    e = grids[i]
    e.grid(row=(i//4)+1, column=i%4, ipady=5)

# Set each grid to numbers 1-15 and blank
setEntries([[i*4+j+1 for j in range(4)] for i in range(4)])
e1.focus_force()
root.mainloop()