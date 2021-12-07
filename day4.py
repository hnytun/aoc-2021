import re
from collections import Counter

file1 = open('input/input4', 'r')

lines = file1.read().splitlines()
drawn = lines[0].split(",")
lines[:] = [x for x in lines if x != ""]
matrix=[]
for line in lines[1:]:
    arr = line.split(" ")
    arr[:] = [x for x in arr if x!= '']
    matrix.append(arr)

boards=[]
currentBoard=[]
for i in range(len(matrix)):
    currentBoard.append(matrix[i])
    if(i != 0 and (i+1)%5==0):
        boards.append(currentBoard.copy())
        currentBoard.clear()


class Bingoboard:

    def __init__ (self,board):
        self.board = board
        self.marks = []
        self.xmarks=[]
        self.ymarks=[]

    def showBoard(self):
        print("--------")
        for row in self.board:
            print(row)
        print("--------")

    def addMarks(self,drawnNumber):
        for x in range(0,5):
            for y in range(0,5):
                if(int(self.board[x][y]) == int(drawnNumber)):
                    self.marks.append((x,y))
                    self.xmarks.append(x)
                    self.ymarks.append(y)
    def getMarks(self):
        return self.marks

    def getSumOfUnmarked(self):
        sum=0
        for x in range(0,5):
            for y in range(0,5):
                if((x,y) not in self.marks):
                    sum+=int(self.board[x][y])
        return sum

    def checkWin(self):
        xdict = Counter(self.xmarks)
        ydict = Counter(self.ymarks)
        for key,value in xdict.items():
            if(value == 5):
                return True
        for key,value in ydict.items():
            if(value == 5):
                return True
        return False


#make all bingoboards
bingoboards=[]
for board in boards:
    bingoboards.append(Bingoboard(board))

winningBoards = []
for bingoNum in drawn:
        for bingoboard in bingoboards:
            bingoboard.addMarks(bingoNum)
            if(bingoboard.checkWin() == True):
                winSum = bingoboard.getSumOfUnmarked()*int(bingoNum)
                bingoboards = [x for x in bingoboards if x!=bingoboard]
                print(winSum)
