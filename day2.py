file1 = open('input/input2', 'r')
lines = file1.read().splitlines()

horizontal=0
depth=0
aim=0
for line in lines:
    direction = line.split(" ")[0]
    distance = int(line.split(" ")[1])
    print(direction,distance)
    if(direction=="forward"):
        horizontal+=distance
        depth+=aim*distance
    elif(direction=="up"):
        aim-=distance
    elif(direction=="down"):
        aim+=distance
print(horizontal*depth)
