file1 = open('input/input1', 'r')
lines = file1.read().splitlines()

#part 1
increments=0
for current,previous in zip(lines[1:],lines):
    if(int(current)>int(previous)):
        increments+=1
print(increments)

#part 2
increments=0
previoussum=0
currentsum=0
for current,previous,previouser in zip(lines[2:],lines[1:],lines):
    currentsum = int(current)+int(previous)+int(previouser)
    if(currentsum != 0 and previoussum !=0 and currentsum>previoussum):
        increments+=1
    previoussum=currentsum
print(increments)