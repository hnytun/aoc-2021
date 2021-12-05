file1 = open('input/input5', 'r')

lines = file1.read().splitlines()

coords =[]
for line in lines:
    split = line.split("->")
    first=split[0].replace(' ','')
    second=split[1].replace(' ','')
    coords.append((int(first.split(",")[0]),int(first.split(",")[1]),int(second.split(",")[0]),int(second.split(",")[1])))

def getline(x0, y0, x1, y1):
    deltax = x1-x0
    dxsign = int(abs(deltax)/deltax)
    deltay = y1-y0
    dysign = int(abs(deltay)/deltay)
    deltaerr = abs(deltay/deltax)
    error = 0
    y = y0
    for x in range(x0, x1, dxsign):
        yield x, y
        error = error + deltaerr
        while error >= 0.5:
            y += dysign
            error -= 1
    yield x1, y1

print("-----------------")

h,w = 1000,1000
#map board

xaxis=list()
for x in range(0,w):
    xaxis.append(list())

for list in xaxis:
    for y in range(0,h):
        list.append(0)

for coord in coords:
    x1 = coord[0]
    y1 = coord[1]
    x2 = coord[2]
    y2 = coord[3]

    #horizontal and vertical
    if(x1 == x2 and y1 == y2):
        xaxis[y1][x1]+=1
        continue

    if(x1 == x2):
        if(y1 < y2):
            for i in range(y1,y2+1):
                xaxis[i][x1]+=1
        else:
            for i in range(y2,y1+1):
                xaxis[i][x1]+=1
    if(y1 == y2):
        if(x1<x2):
            for i in range(x1,x2+1):
                xaxis[y1][i]+=1
        else:
            for i in range(x2,x1+1):
                xaxis[y1][i]+=1
    #diagonal
    if(x1 != x2 and y1 != y2):
        for i in getline(x1,y1,x2,y2):
            xaxis[i[1]][i[0]]+=1

counter=0
for xline in xaxis:
    for yline in xline:
         if(yline > 1):
             counter+=1
print(counter)








