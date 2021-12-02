file1 = open('input/input2', 'r')
lines = file1.read().splitlines()

print(lines)
#part 1 and 2, commented lines is part 1
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
        print("added " + str(distance) + " to horizontal")
    elif(direction=="up"):
        #depth-=distance
        aim-=distance
        print("decreased " + str(distance) + " to depth")
    elif(direction=="down"):
        #depth+=distance
        aim+=distance
        print("added " + str(distance) + " to depth")
print(horizontal*depth)
