from random import randint
from copy import deepcopy
class rubiksCube:
    def __init__(self):
        self.frontFace = [['g','g','g'],['g','g','g'],['g','g','g']]
        self.backFace = [['b','b','b'],['b','b','b'],['b','b','b']]
        self.leftFace = [['o','o','o'],['o','o','o'],['o','o','o']]
        self.rightFace = [['r','r','r'],['r','r','r'],['r','r','r']]
        self.topFace = [['w','w','w'],['w','w','w'],['w','w','w']]
        self.botFace = [['y','y','y'],['y','y','y'],['y','y','y']]

    def resetCube(self):
        self.frontFace = [['g','g','g'],['g','g','g'],['g','g','g']]
        self.backFace = [['b','b','b'],['b','b','b'],['b','b','b']]
        self.leftFace = [['o','o','o'],['o','o','o'],['o','o','o']]
        self.rightFace = [['r','r','r'],['r','r','r'],['r','r','r']]
        self.topFace = [['w','w','w'],['w','w','w'],['w','w','w']]
        self.botFace = [['y','y','y'],['y','y','y'],['y','y','y']]

    def faceTurn(self,sideS):
        proxyA = []
        proxyB = []
        proxyC = []

        if sideS == 'right': #right
            side = 2
            self.clockwiseTurn(self.rightFace)
            for r in range(len(self.frontFace)):
                proxyA.append(self.get(side,r,self.frontFace))
                self.set(side,r,self.get(side,r,self.botFace),self.frontFace)
                
            for r in range(len(self.topFace)):
                proxyB.append(self.get(side,r,self.topFace))
                self.set(side,r,proxyA[r],self.topFace)

            for r in range(len(self.backFace)):
                proxyC.append(self.get(side,r,self.backFace))
                self.set(side,r,proxyB[r],self.backFace)

            for r in range(len(self.botFace)):
                self.set(side,r,proxyC[r],self.botFace)
            return 'R'
        elif sideS == 'left': #left
            side = 0
            self.clockwiseTurn(self.leftFace)
            for r in range(len(self.frontFace)):
                proxyA.append(self.get(side,r,self.frontFace))
                self.set(side,r,self.get(side,r,self.topFace),self.frontFace)

            for r in range(len(self.botFace)):
                proxyB.append(self.get(side,r,self.botFace))
                self.set(side,r,proxyA[r],self.botFace)

            for r in range(len(self.backFace)):
                proxyC.append(self.get(side,r,self.backFace))
                self.set(side,r,proxyB[r],self.backFace)

            for r in range(len(self.topFace)):
                self.set(side,r,proxyC[r],self.topFace)     
            return 'L'
        elif sideS == 'top':
            side = 0
            self.clockwiseTurn(self.topFace)

            for c in range(len(self.frontFace)):
                proxyA.append(self.get(c,side,self.frontFace))
                self.set(c,side,self.get(c,side,self.rightFace),self.frontFace)

            for c in range(len(self.leftFace)):
                proxyB.append(self.get(c,side,self.leftFace))
                self.set(c,side,proxyA[c],self.leftFace)

            proxyB = proxyB[::-1]
            for c in range(len(self.backFace)):
                proxyC.append(self.get(c,side+2,self.backFace))
                self.set(c,side+2,proxyB[c],self.backFace)

            proxyC = proxyC[::-1]
            for c in range(len(self.rightFace)):
                self.set(c,side,proxyC[c],self.rightFace)   
            return 'T'
        elif sideS == 'bottom':
            side = 2
            self.clockwiseTurn(self.botFace)
            for c in range(len(self.frontFace)):
                proxyA.append(self.get(c,side,self.frontFace))
                self.set(c,side,self.get(c,side,self.leftFace),self.frontFace)

            for c in range(len(self.rightFace)):
                proxyB.append(self.get(c,side,self.rightFace))
                self.set(c,side,proxyA[c],self.rightFace)

            proxyB = proxyB[::-1]
            for c in range(len(self.backFace)):
                proxyC.append(self.get(c,side-2,self.backFace))
                self.set(c,side-2,proxyB[c],self.backFace)

            proxyC = proxyC[::-1]
            for c in range(len(self.leftFace)):
                self.set(c,side,proxyC[c],self.leftFace)   
            return 'D'
        elif sideS == 'front':
                #side is not set number
            self.clockwiseTurn(self.frontFace)
            for i in range(len(self.topFace)):
                proxyA.append(self.get(i,2,self.topFace))
                self.set(i,2,self.get(2,2-i,self.leftFace),self.topFace)

            for i in range(len(self.rightFace)):
                proxyB.append(self.get(0,i,self.rightFace))
                self.set(0,i,proxyA[i],self.rightFace)
            proxyB = proxyB[::-1]
            for i in range(len(self.botFace)):
                proxyC.append(self.get(i,0,self.botFace))
                self.set(i,0,proxyB[i],self.botFace)

            for i in range(len(self.leftFace)):
                self.set(2,i,proxyC[i],self.leftFace)   
            return 'F'
        elif sideS == 'back':
            self.clockwiseTurn(self.backFace)

            for i in range(len(self.topFace)):
                proxyA.append(self.get(i,0,self.topFace))

                self.set(i,0,self.get(2,i,self.rightFace),self.topFace)

            proxyA = proxyA[::-1]
            for i in range(len(self.leftFace)):
                proxyB.append(self.get(0,i,self.leftFace))
                self.set(0,i,proxyA[i],self.leftFace)

            for i in range(len(self.botFace)):
                proxyC.append(self.get(i,2,self.botFace))
                self.set(i,2,proxyB[i],self.botFace)

            proxyC = proxyC[::-1]
            for i in range(len(self.rightFace)):
                self.set(2,i,proxyC[i],self.rightFace)   
            return 'B'
        
    def primeFaceTurn(self,move):
        for i in range(3):
            self.faceTurn(move)
        if move == 'left':
            return 'l'
        elif move == 'right':
            return 'r'
        elif move == 'top':
            return 't'
        elif move == 'bottom':
            return 'd'
        elif move == 'front':
            return 'f'
        elif move == 'back':
            return 'b'

    def rotateCube(self,direction):
        if direction == 'left':
            self.countClockTurn(self.topFace)
            self.clockwiseTurn(self.botFace)

            proxy = deepcopy(self.frontFace)
            self.frontFace = deepcopy(self.leftFace)
            self.leftFace = deepcopy(self.backFace)
            self.backFace = deepcopy(self.rightFace)
            self.rightFace = proxy
            
            self.clockwiseTurn(self.leftFace)
            self.clockwiseTurn(self.leftFace)

            self.clockwiseTurn(self.backFace)
            self.clockwiseTurn(self.backFace)  
        else:
            pass
        return 'RL'

    def rotateCubeR(self):
        for i in range(3):
            self.rotateCube('left')  
        return 'RR'


    def flipCube(self):
        self.clockwiseTurn(self.leftFace)
        self.clockwiseTurn(self.leftFace)

        self.clockwiseTurn(self.rightFace)
        self.clockwiseTurn(self.rightFace)

        proxy = self.topFace
        self.topFace = deepcopy(self.botFace)
        self.botFace = proxy

        proxy = self.frontFace
        self.frontFace = deepcopy(self.backFace)
        self.clockwiseTurn(self.backFace)
        self.clockwiseTurn(self.backFace)       
        self.backFace = proxy
        return "FC"

    """
       2             1
    1     3   ->  4     2
       4             3
    """
    def clockwiseTurn(self,face):
        #rotating side pieces
        sq1 = self.get(0,1,face)  
        sq2 = self.get(1,0,face)
        sq3 = self.get(2,1,face)
        sq4 = self.get(1,2,face)
        self.set(0,1,sq4,face) #1
        self.set(1,0,sq1,face) #2
        self.set(2,1,sq2,face) #3 
        self.set(1,2,sq3,face) #4

        sq1 = self.get(0,0,face)  
        sq2 = self.get(2,0,face)
        sq3 = self.get(2,2,face)
        sq4 = self.get(0,2,face)
        self.set(0,0,sq4,face) #1
        self.set(2,0,sq1,face) #2
        self.set(2,2,sq2,face) #3 
        self.set(0,2,sq3,face) #4

    def countClockTurn(self,face):
            self.clockwiseTurn(face)
            self.clockwiseTurn(face)
            self.clockwiseTurn(face)

    def get(self,x,y,face):
        return face[y][x]

    def set(self,x,y,val,face):
        face[y][x] = val

    def shuffleCube(self):
        moves = []
        for i in range(10):
            moves += self.chooseTurn(randint(1,12))
        return moves
        
    def chooseTurn(self,turn):
        if turn == 1:
            self.faceTurn('left')
            return 'L'
        elif turn == 2:
            self.faceTurn('right')
            return 'R'
        elif turn == 3:
            self.faceTurn('top')
            return 'T'
        elif turn == 4:
            self.faceTurn('bottom')
            return 'D'
        elif turn == 5:
            self.faceTurn('front')
            return 'F'
        elif turn == 6:
            self.faceTurn('back')
            return 'B'
        elif turn == 7:
            self.primeFaceTurn('left')
            return 'l'
        elif turn == 8:
            self.primeFaceTurn('right')
            return 'r'
        elif turn == 9:
            self.primeFaceTurn('top')
            return 't'
        elif turn == 10:
            self.primeFaceTurn('bottom')
            return 'd'
        elif turn == 11:
            self.primeFaceTurn('front')
            return 'f'
        elif turn == 12:
            self.primeFaceTurn('back')
            return 'b'
    
    def printCube(self):
        for y in range(len(self.topFace)):
            print("      ",end="")
            for x in range(len(self.topFace)):
                print(f"{self.get(x,y,self.topFace)} ", end = "")
            print("")

        for y in range(len(self.leftFace)):
            for x in range(len(self.frontFace*3)):
                if x <= 2:
                    print(f"{self.get(x,y,self.leftFace)} ", end="")
                elif x in range(3,6):
                    print(f"{self.get(x-3,y,self.frontFace)} ", end="")
                else:
                    print(f"{self.get(x-6,y,self.rightFace)} ", end="")
            print("")

        for y in range(len(self.botFace)):
            print("      ",end="")
            for x in range(len(self.botFace)):
                print(f"{self.get(x,y,self.botFace)} ", end = "")
            print("")

            
        for y in range(len(self.backFace)):
            print("      ",end="")
            for x in range(len(self.backFace)):
                print(f"{self.get(x,y,self.backFace)} ", end = "")
            print("")
        print("--------------")

    def doMoveSet(self,moveSet):
        for turn in moveSet:
            if turn == 'L':
                self.faceTurn('left')
            elif turn == 'R':
                self.faceTurn('right')
            elif turn == 'T':
                self.faceTurn('top')
            elif turn == 'D':
                self.faceTurn('bottom')
            elif turn == 'F':
                self.faceTurn('front')
            elif turn == 'B':
                self.faceTurn('back')
            elif turn == 'l':
                self.primeFaceTurn('left')
            elif turn == 'r':
                self.primeFaceTurn('right')
            elif turn == 't':
                self.primeFaceTurn('top')
            elif turn == 'd':
                self.primeFaceTurn('bottom')
            elif turn == 'f':
                self.primeFaceTurn('front')
            elif turn == 'b':
                self.primeFaceTurn('back')
            elif turn == 'RL':
                self.rotateCube('left')
            elif turn == 'RR':
                self.rotateCubeR()
            elif turn == 'FC':
                self.flipCube()
