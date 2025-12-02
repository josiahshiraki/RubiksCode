from RubiksCube import rubiksCube

class SolveCube:
    def __init__(self,cube):
        self.cube = cube

    def whiteCross(self):
        solve = [1]
        rCube = self.cube
        
        solve[0] = rCube.flipCube()
        x = 1
        while rCube.get(0,1,rCube.topFace) != 'w' or rCube.get(2,1,rCube.topFace) != 'w' or rCube.get(1,2,rCube.topFace) != 'w' or rCube.get(1,0,rCube.topFace) != 'w':
            if rCube.get(0,1,rCube.frontFace) == 'w': #front (0,1)
                while rCube.get(0,1,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('left')
            elif rCube.get(2,1,rCube.frontFace) == 'w': #front (2,1)
                while rCube.get(2,1,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.faceTurn('right')
            elif rCube.get(0,1,rCube.rightFace) == 'w': #right side (0,1)
                while rCube.get(1,2,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('front')
            elif rCube.get(2,1,rCube.leftFace) == 'w': #left face (2,1)
                while rCube.get(1,2,rCube.topFace) == 'w': 
                    solve += rCube.faceTurn('top')
                solve += rCube.faceTurn('front')
            elif rCube.get(1,0,rCube.frontFace) == 'w': #front face (1,0)
                while rCube.get(1,2,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('front')
                while rCube.get(0,1,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('left')
            elif rCube.get(1,2,rCube.frontFace) == 'w': #front face (1,2)
                while rCube.get(1,2,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('front')
                while rCube.get(0,1,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('left')
            elif rCube.get(1,0,rCube.botFace) == 'w': #bot face (1,0)
                while rCube.get(1,2,rCube.topFace) == 'w':
                    solve += rCube.faceTurn('top')
                solve += rCube.primeFaceTurn('front')
                solve += rCube.primeFaceTurn('front')
            else:
                solve.append(rCube.rotateCube('left'))
            if x > 20: 
                break #prevent infinity loop 
            x+=1
        while rCube.get(1,1,rCube.frontFace) != 'r':
            solve.append(rCube.rotateCube('left'))

        #code can be optimized to one while loop in a seperate function
        while rCube.get(1,0,rCube.frontFace) != 'r' or rCube.get(1,2,rCube.topFace) != 'w':
            solve += rCube.faceTurn('top')
        solve += rCube.faceTurn('front')
        solve += rCube.faceTurn('front')

        while rCube.get(1,0,rCube.leftFace) != 'b' or rCube.get(0,1,rCube.topFace) != 'w':
            solve += rCube.faceTurn('top')
        solve += rCube.faceTurn('left')
        solve += rCube.faceTurn('left') 

        while rCube.get(1,0,rCube.rightFace) != 'g' or rCube.get(2,1,rCube.topFace) != 'w':
            solve += rCube.faceTurn('top')
        solve += rCube.faceTurn('right')
        solve += rCube.faceTurn('right')   

        while rCube.get(1,2,rCube.backFace) != 'o' or rCube.get(1,0,rCube.topFace) != 'w':
            solve += rCube.faceTurn('top')
        solve += rCube.faceTurn('back')
        solve += rCube.faceTurn('back')             

        solve.append(rCube.flipCube())
        return solve
    
    #inserted cube will already have been flipped so that white is on top
    def whiteCorners(self):
        solve = []
        rCube = self.cube
        x = 0
        while x < 10:
            if rCube.get(0,2,rCube.frontFace) == 'w':
                solve.append(rCube.rotateCube('left'))
                self.insertWhiteCorner(rCube,'left',solve)
            elif rCube.get(2,2,rCube.frontFace) == 'w':
                solve.append(rCube.rotateCubeR())
                self.insertWhiteCorner(rCube,'right',solve)
            elif rCube.get(0,0,rCube.frontFace) == 'w': #front face top left
                print('FOUND TOP LEFT')
                solve += rCube.primeFaceTurn('front')
                solve += rCube.primeFaceTurn('bottom')
                solve += rCube.faceTurn('front')
                solve += rCube.faceTurn('bottom')
                rCube.printCube()

                solve.append(rCube.rotateCube('left'))
                self.insertWhiteCorner(rCube,'left',solve)
            elif rCube.get(2,0,rCube.frontFace) == 'w': #front face top right

                print('FOUND TOP RIGHT') 
                rCube.printCube()
                solve += rCube.faceTurn('front')
                solve += rCube.faceTurn('bottom')
                solve += rCube.primeFaceTurn('front')
                solve += rCube.primeFaceTurn('bottom')

                rCube.printCube()
                solve.append(rCube.rotateCubeR())
                self.insertWhiteCorner(rCube,'right',solve)
            
            elif rCube.get(0,2,rCube.topFace) == 'w' and rCube.get(0,0,rCube.frontFace) != rCube.get(1,1,rCube.frontFace): #top face left
                print("FOUND TOP LEFT")
                rCube.printCube()
                solve += rCube.faceTurn('left')
                solve += rCube.faceTurn('bottom')
                solve += rCube.primeFaceTurn('left')
                solve += rCube.primeFaceTurn('bottom')
                solve.append(rCube.rotateCube('left'))
                rCube.printCube()
                self.insertWhiteCorner(rCube,'left',solve)

            elif rCube.get(2,2,rCube.topFace) == 'w' and rCube.get(2,0,rCube.frontFace) != rCube.get(1,1,rCube.frontFace): #top face right
                print("FOUND TOP RIGHT")
                solve += rCube.primeFaceTurn('right')
                solve += rCube.primeFaceTurn('bottom')
                solve += rCube.faceTurn('right')
                solve += rCube.faceTurn('bottom')
                solve.append(rCube.rotateCubeR())
                self.insertWhiteCorner(rCube,'right',solve)

            elif rCube.get(0,0,rCube.botFace) == 'w': #bot left
                print('FOUND BOT LEFT')
                rCube.printCube()
                while rCube.get(2,0,rCube.topFace) == 'w':
                    solve += rCube.primeFaceTurn('bottom')
                    solve.append(rCube.rotateCube('left'))

                solve += rCube.primeFaceTurn('front')
                solve += rCube.faceTurn('bottom')
                solve += rCube.faceTurn('front')
                solve += rCube.faceTurn('bottom')
                solve += rCube.faceTurn('bottom')
                solve.append(rCube.rotateCube('left'))
                self.insertWhiteCorner(rCube,'left',solve)

            elif rCube.get(2,0,rCube.botFace) == 'w': #bot right
                rCube.printCube()
                while rCube.get(2,2,rCube.topFace) == 'w':
                    solve += rCube.primeFaceTurn('bottom')
                    solve.append(rCube.rotateCube('left'))

                solve += rCube.faceTurn('front')
                solve += rCube.primeFaceTurn('bottom')
                solve += rCube.primeFaceTurn('front')
                solve += rCube.faceTurn('bottom')
                solve += rCube.faceTurn('bottom')

                solve.append(rCube.rotateCubeR())
                self.insertWhiteCorner(rCube,'right',solve) 
            else:
                solve.append(rCube.rotateCube('left'))
            x+=1   
        solve.append(rCube.flipCube())
        return solve  

    def insertWhiteCorner(self,rCube,direction,solve):
        if direction == 'left':
            rCube.printCube()
            while rCube.get(2,2,rCube.frontFace) != rCube.get(1,1,rCube.frontFace):
                solve += rCube.primeFaceTurn('bottom')
                solve.append(rCube.rotateCube('left'))

            solve += rCube.faceTurn('bottom')
            solve += rCube.faceTurn('front')
            solve += rCube.primeFaceTurn('bottom')
            solve += rCube.primeFaceTurn('front')
            print('result')
            rCube.printCube()
            print('left found')

        elif direction == 'right':
            while rCube.get(0,2,rCube.frontFace) != rCube.get(1,1,rCube.frontFace):
                solve += rCube.faceTurn('bottom')
                solve.append(rCube.rotateCubeR())
                rCube.printCube()

            solve += rCube.primeFaceTurn('bottom')
            solve += rCube.primeFaceTurn('front')
            solve += rCube.faceTurn('bottom')
            solve += rCube.faceTurn('front')
            rCube.printCube()

    def edges(self):
        solve = []
        rCube = self.cube
        print('_________start_____________')
        for i in range(20):
            if self.isValidEdge(rCube.get(1,0,rCube.frontFace),rCube.get(1,2,rCube.topFace)):
                print('IS VALID EDGE')
                while rCube.get(1,0,rCube.frontFace) != rCube.get(1,1,rCube.frontFace):
                    solve += rCube.faceTurn('top')
                    solve.append(rCube.rotateCube('left'))
                if rCube.get(1,2,rCube.topFace) == rCube.get(1,1,rCube.leftFace):
                    print('execute left')
                    self.insertEdge(rCube,'left',solve)
                else:
                    print('execute right')
                    self.insertEdge(rCube,'right',solve) 
            elif self.isValidEdge(rCube.get(0,1,rCube.frontFace),rCube.get(2,1,rCube.leftFace)) and rCube.get(0,1,rCube.frontFace) != rCube.get(1,1,rCube.frontFace): #valid edge left
                self.insertEdge(rCube,'left',solve)
            elif self.isValidEdge(rCube.get(2,1,rCube.frontFace),rCube.get(0,1,rCube.leftFace)) and rCube.get(2,1,rCube.frontFace) != rCube.get(1,1,rCube.frontFace): #valid edge right
                self.insertEdge(rCube,'right',solve)
            else:  
                solve.append(rCube.rotateCube('left'))
        return solve
    
    def isValidEdge(self,col1,col2):
        if col1 == 'y' or col2 == 'y':
            return False
        return True
    
    def insertEdge(self,rCube,direction,solve):
        if direction == 'left':
            rCube.printCube()
            solve += rCube.primeFaceTurn('top')
            solve += rCube.primeFaceTurn('left')
            solve += rCube.faceTurn('top')
            solve += rCube.faceTurn('left')
            solve += rCube.faceTurn('top')
            solve += rCube.faceTurn('front')
            solve += rCube.primeFaceTurn('top')
            solve += rCube.primeFaceTurn('front')
        else:
            rCube.printCube()
            solve += rCube.faceTurn('top')
            solve += rCube.faceTurn('right')
            solve += rCube.primeFaceTurn('top')
            solve += rCube.primeFaceTurn('right')
            solve += rCube.primeFaceTurn('top')
            solve += rCube.primeFaceTurn('front')
            solve += rCube.faceTurn('top')
            solve += rCube.faceTurn('front')            

        rCube.printCube()
    
    def solveTop(self):
        solution = []
        rCube = self.cube
        print('start')
        top = rCube.get(1,0,rCube.topFace)
        left = rCube.get(0,1,rCube.topFace)
        right = rCube.get(2,1,rCube.topFace)
        bot = rCube.get(1,2,rCube.topFace)
        y = 0
        while top != 'y' or left != 'y' or right != 'y' or bot != 'y':
            if top == 'y' and bot == 'y':
                solution += rCube.faceTurn('top')
            elif top == 'y' and right == 'y':
                solution += rCube.primeFaceTurn('top')
            elif left == 'y' and bot == 'y':
                solution += rCube.faceTurn('top')
            elif right == 'y' and bot == 'y':
                solution += rCube.faceTurn('top')
                solution += rCube.faceTurn('top')
            self.makeCross(rCube,solution)

            rCube.printCube()
            top = rCube.get(1,0,rCube.topFace)
            left = rCube.get(0,1,rCube.topFace)
            right = rCube.get(2,1,rCube.topFace)
            bot = rCube.get(1,2,rCube.topFace)  
            y+=1
            if y == 5: 
                break

        tL,tR = rCube.get(0,0,rCube.topFace),rCube.get(2,0,rCube.topFace)
        bL,bR = rCube.get(0,2,rCube.topFace),rCube.get(2,2,rCube.topFace)
        count = 0
        if tL == 'y':  
            count+=1
        if tR == 'y':
            count+=1
        if bL == 'y':
            count+=1
        if bR == 'y':
            count+=1
        
        while tL != 'y' or tR != 'y' or bL != 'y' or bR != 'y':
            tL,tR = rCube.get(0,0,rCube.topFace),rCube.get(2,0,rCube.topFace)
            bL,bR = rCube.get(0,2,rCube.topFace),rCube.get(2,2,rCube.topFace)
            count = 0

            if tL == 'y':
                count+=1
            if tR == 'y':
                count+=1
            if bL == 'y':
                count+=1
            if bR == 'y':
                count+=1

            if count == 1:
                while rCube.get(0,2,rCube.topFace) != 'y':
                    solution += rCube.faceTurn('top')
                self.solveYellowCorners(rCube,solution)
            elif count == 2:
                while rCube.get(0,0,rCube.frontFace) != 'y':
                    solution += rCube.faceTurn('top')
                self.solveYellowCorners(rCube,solution)
            elif count == 0:
                while rCube.get(2,0,rCube.leftFace) != 'y':
                    solution += rCube.faceTurn('top')
                self.solveYellowCorners(rCube,solution)
        rCube.printCube()
        return solution

    def solveYellowCorners(self,rCube,solution):
        solution += rCube.faceTurn('right')
        solution += rCube.faceTurn('top')
        solution += rCube.primeFaceTurn('right')
        solution += rCube.faceTurn('top')
        solution += rCube.faceTurn('right')
        solution += rCube.faceTurn('top')
        solution += rCube.faceTurn('top')
        solution += rCube.primeFaceTurn('right')        
    
    def makeCross(self,rCube,solution):
        solution += rCube.faceTurn('front')
        solution += rCube.faceTurn('top')
        solution += rCube.faceTurn('right')
        solution += rCube.primeFaceTurn('top')
        solution += rCube.primeFaceTurn('right')
        solution += rCube.primeFaceTurn('front')

    def solvePLL(self):
        solution = []
        rCube = self.cube

        rCube.printCube()
        if rCube.get(0,0,rCube.frontFace) != rCube.get(2,0,rCube.frontFace) or rCube.get(0,0,rCube.rightFace) != rCube.get(2,0,rCube.rightFace):
            backFaceL,backFaceR = rCube.get(0,2,rCube.backFace),rCube.get(2,2,rCube.backFace)
            for i in range(4):
                if backFaceL == backFaceR:
                    break
                else:
                    solution += rCube.faceTurn('top')
                backFaceL,backFaceR = rCube.get(0,2,rCube.backFace),rCube.get(2,2,rCube.backFace)

            if backFaceL == backFaceR:
                self.makeHeadlights(rCube,solution)
            else: #algorithm no headlights found
                self.makeHeadlights(rCube,solution)
                for i in range(4):
                    if backFaceL == backFaceR:
                        break
                    else:
                        solution += rCube.faceTurn('top')
                    backFaceL,backFaceR = rCube.get(0,2,rCube.backFace),rCube.get(2,2,rCube.backFace)
                self.makeHeadlights(rCube,solution)

        rCube.printCube()

        if rCube.get(0,2,rCube.backFace) == rCube.get(1,2,rCube.backFace) == rCube.get(2,2,rCube.backFace):
            if rCube.get(0,0,rCube.frontFace) == rCube.get(1,0,rCube.frontFace) == rCube.get(2,0,rCube.frontFace):
                return solution
        
        #can be refactored, the code below can be moved to a seperate function and called twice
        for i in range(4):
            if rCube.get(0,2,rCube.backFace) == rCube.get(1,2,rCube.backFace) == rCube.get(2,2,rCube.backFace):
                if rCube.get(1,0,rCube.frontFace) == rCube.get(0,0,rCube.rightFace):
                    rCube.printCube()
                    self.finalAlgo(rCube,'right',solution)
                    rCube.printCube()
                    return solution
                else:
                    rCube.printCube()
                    self.finalAlgo(rCube,'left',solution)
                    rCube.printCube()
                    return solution
            solution += rCube.faceTurn('top')

        #none found, all headlights

        if rCube.get(0,2,rCube.backFace) == rCube.get(1,2,rCube.backFace) == rCube.get(2,2,rCube.backFace):
            if rCube.get(0,0,rCube.frontFace) == rCube.get(1,0,rCube.frontFace) == rCube.get(2,0,rCube.frontFace):
                return solution

        rCube.printCube()    
        self.finalAlgo(rCube,'right',solution)
        rCube.printCube()

        for i in range(4):
            if rCube.get(0,2,rCube.backFace) == rCube.get(1,2,rCube.backFace) == rCube.get(2,2,rCube.backFace):
                if rCube.get(1,0,rCube.frontFace) == rCube.get(0,0,rCube.rightFace):
                    self.finalAlgo(rCube,'right',solution)
                    return solution
                else:
                    self.finalAlgo(rCube,'left',solution)
                    return solution
            solution += rCube.faceTurn('top')
        
        #ERROR = 1/0


    def makeHeadlights(self,rCube,solution):
        solution += rCube.primeFaceTurn('right')
        solution += rCube.faceTurn('front')
        solution += rCube.primeFaceTurn('right')
        solution += rCube.faceTurn('back')
        solution += rCube.faceTurn('back')

        solution += rCube.faceTurn('right')
        solution += rCube.primeFaceTurn('front')
        solution += rCube.primeFaceTurn('right')
        solution += rCube.faceTurn('back')
        solution += rCube.faceTurn('back')

        solution += rCube.faceTurn('right')
        solution += rCube.faceTurn('right')
        solution += rCube.primeFaceTurn('top')

    def finalAlgo(self,rCube,direction,solution):
        if direction == 'left':
            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('top')
            solution += rCube.faceTurn('left')
            solution += rCube.primeFaceTurn('right')

            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')
            solution += rCube.primeFaceTurn('left')
            solution += rCube.faceTurn('right')
            solution += rCube.faceTurn('top')
            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')

        elif direction == 'right':
            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')
            solution += rCube.primeFaceTurn('top')
            solution += rCube.faceTurn('left')
            solution += rCube.primeFaceTurn('right')

            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')
            solution += rCube.primeFaceTurn('left')
            solution += rCube.faceTurn('right')
            solution += rCube.primeFaceTurn('top')
            solution += rCube.faceTurn('front')
            solution += rCube.faceTurn('front')


cube = rubiksCube()
print(cube.shuffleCube())
#cube.doMoveSet(['D', 'l', 't', 'D', 'f', 'D', 'f', 'l', 'l', 'L'])
solution = SolveCube(cube)
solution.whiteCross()
solution.whiteCorners()
cube.printCube()
solution.edges()
solution.solveTop()
solution.solvePLL()
cube.printCube()


    
