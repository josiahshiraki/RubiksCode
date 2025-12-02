from RubiksCube import rubiksCube
from tkinter import Canvas
import tkinter as tk
from SolveCube import SolveCube
from tkinter import messagebox



#-------------set up-----------------
class MyGUI:

    def __init__(self):
        self.cube = rubiksCube()
        self.solution = SolveCube(self.cube)
        
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Cube Scrambler")

        self.canvas = Canvas(self.root)

        self.shuffle = tk.StringVar(self.root)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        buttonFrame = tk.Frame(self.root)
        buttonFrame.columnconfigure(0,weight=1)
        buttonFrame.columnconfigure(1,weight=1)
        buttonFrame.columnconfigure(2,weight=1)

        button1 = tk.Button(buttonFrame, text='scramble', font=('Arial',18),command= self.scramble)
        button1.grid(row=0,column=0,sticky=tk.W+tk.E)

        button2 = tk.Button(buttonFrame, text='white Cross', font=('Arial',18),command=self.solveWhiteCross)
        button2.grid(row=0,column=1,sticky=tk.W+tk.E)

        button3 = tk.Button(buttonFrame, text='white Corners', font=('Arial',18),command=self.solveWhiteCorners)
        button3.grid(row=0,column=2,sticky=tk.W+tk.E)

        button4 = tk.Button(buttonFrame, text='edges', font=('Arial',18),command=self.solveEdges)
        button4.grid(row=1,column=0,sticky=tk.W+tk.E)

        button5 = tk.Button(buttonFrame, text='top', font=('Arial',18),command=self.solveTop)
        button5.grid(row=1,column=1,sticky=tk.W+tk.E)

        button6 = tk.Button(buttonFrame, text='PLL', font=('Arial',18),command=self.solvePLL)
        button6.grid(row=1,column=2,sticky=tk.W+tk.E)


        buttonFrame.pack(fill='x')

        label = tk.Label(self.root, text = "Press buttons in this order: scramble->white cross->white corners->edges->top->PLL", font=('Arial',12))
        label.pack()

        self.root.mainloop()

    def solveWhiteCross(self):
        self.cube.printCube()
        solveW = self.solution.whiteCross()

        self.shuffle.set(', '.join(solveW))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="solve white Cross",message=self.shuffle.get())

    def solveWhiteCorners(self):
        self.cube.printCube()
        solveW = self.solution.whiteCorners()

        self.shuffle.set(', '.join(solveW))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="solve white Corners",message=self.shuffle.get())

    def solveEdges(self):
        self.cube.printCube()
        solveW = self.solution.edges()

        self.shuffle.set(', '.join(solveW))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="solve edges",message=self.shuffle.get())

    def solveTop(self):
        self.cube.printCube()
        solveW = self.solution.solveTop()

        self.shuffle.set(', '.join(solveW))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="solve top",message=self.shuffle.get())

    def solvePLL(self):
        self.cube.printCube()
        solveW = self.solution.solvePLL()

        self.shuffle.set(', '.join(solveW))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="solve PLL",message=self.shuffle.get())
        
    def scramble(self):
        self.cube.resetCube()
        self.cube.printCube()
        scramble = self.cube.shuffleCube()

        self.shuffle.set(', '.join(scramble))
        print(self.shuffle.get())
        self.printWhole(self.cube)
        messagebox.showinfo(title="SCRAMBLE",message=self.shuffle.get())



    def printFace(self,face,x1,y1,x2,y2):
        for i in range(3):
            for j in range(3):
                step = j*20
                self.canvas.create_rectangle(x1+step,y1,x2+step,y2,fill= self.findColor(face[i][j]))
            y1 += 20
            y2 += 20

    def printWhole(self,cube): 
        self.printFace(cube.topFace,100,100,120,120)
        self.printFace(cube.leftFace,40,160,60,180)
        self.printFace(cube.frontFace,100,160,120,180)
        self.printFace(cube.rightFace,160,160,180,180)
        self.printFace(cube.botFace,100,220,120,240)
        self.printFace(cube.backFace,100,280,120,300)
        
    #---------------moveset-------------------
    def doMoveSet(self,cube,moveSet):
        for turn in moveSet:                
            if turn == 'L':
                cube.faceTurn('left')
            elif turn == 'R':
                cube.faceTurn('right')
            elif turn == 'T':
                cube.faceTurn('top')
            elif turn == 'D':
                cube.faceTurn('bottom')
            elif turn == 'F':
                cube.faceTurn('front')
            elif turn == 'B':
                cube.faceTurn('back')
            elif turn == 'l':
                cube.primeFaceTurn('left')
            elif turn == 'r':
                cube.primeFaceTurn('right')
            elif turn == 't':
                cube.primeFaceTurn('top')
            elif turn == 'd':
                cube.primeFaceTurn('bottom')
            elif turn == 'f':
                cube.primeFaceTurn('front')
            elif turn == 'b':
                cube.primeFaceTurn('back')
            elif turn == 'RL':
                cube.rotateCube('left')
            elif turn == 'RR':
                cube.rotateCubeR()
            elif turn == 'FC':
                cube.flipCube()
    #--------------------------------------------
    def findColor(self,char):
        if char == 'w':
            return 'white'
        elif char == 'r':
            return 'red'
        elif char == 'g':
            return 'green'
        elif char == 'y':
            return 'yellow'
        elif char == 'o':
            return 'orange'
        elif char == 'b':
            return 'blue'
        
MyGUI()
        
# cube = rubiksCube()
# print(cube.get(0,0,cube.topFace))

# cube.printCube()
# scramble = cube.shuffleCube()
# print('orig--------------------')
# cube.printCube()
# print(scramble)
# solution = SolveCube(cube)
# solve = solution.whiteCross()
# solveWC = solution.whiteCorners()
# solveE = solution.edges()
# solveT = solution.solveTop()
# solvePll = solution.solvePLL()

# #executes saved moveset
# cube.resetCube()
# cube.doMoveSet(scramble)
# print('copied---------------------')
# cube.printCube()
# print('---------Start-------------')
# page = myGUI()
# page.doMoveSet(cube,solve)
# page.doMoveSet(cube,solveWC)
# page.doMoveSet(cube,solveE)
# page.doMoveSet(cube,solveT)
# page.doMoveSet(cube,solvePll)

# print(solve)
# print(solveWC)
# print(solveE)
# print(solveT)
# print(solvePll)

# page.printWhole(cube)

# page.root.mainloop()
