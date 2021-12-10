file = open('input/input9_sample', 'r')
input = [line.replace("\n","") for line in file.readlines() if line.strip()]

def createMatrix(input):
    matrix=list()
    for x in range(0,len(input[0])):
        matrix.append(list())
        for y in range(0,len(input)):
            matrix[x].append(0)
            matrix[x][y] = int(input[y][x])
    return matrix

def GetPointValue(point,matrix):
    return matrix[point[0]][point[1]]

def findAdjacents(point,matrix):
    adjacents=[]
    if(point[0] != 0):
        adjacents.append(matrix[point[0]-1][point[1]])#left
    if(point[0] != len(matrix)-1):
        adjacents.append(matrix[point[0]+1][point[1]])#right
    if(point[1] != len(matrix[0])-1):
        adjacents.append(matrix[point[0]][point[1]+1])#down
    if(point[1] != 0):
        adjacents.append(matrix[point[0]][point[1]-1])#top
    """
    dont need to check these?
    if(point[1] != 0 and point[0] != 0):
        adjacents.append(matrix[point[0]-1][point[1]-1])#topLeft
    if(point[1] != 0 and point[0] != len(matrix)-1):
        adjacents.append(matrix[point[0]+1][point[1]-1])#topRight
    if(point[1] != len(matrix[0])-1 and point[0] != 0):
        adjacents.append(matrix[point[0]-1][point[1]+1])#downLeft
    if(point[1] != len(matrix[0])-1 and point[0] != len(matrix)-1):
        adjacents.append(matrix[point[0]+1][point[1]+1])#downRight
    """
    return adjacents

def isLowPoint(point,matrix):
    lowPoint=True
    adjacents = findAdjacents(point,matrix)
    for adjacent in adjacents:
        if(adjacent <= GetPointValue(point,matrix)):
            return False
    return True

def getLowPoints(matrix):
    lowPoints=[]
    for x in range(0,len(matrix)):
        for y in range(0,len(matrix[1])):
            if(isLowPoint((x,y),matrix)):
                lowPoints.append((x,y))
    return lowPoints

matrix = createMatrix(input)

print(getLowPoints(matrix))
