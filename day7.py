import numpy as np
file1 = open('input/input7', 'r')
lines = file1.read().splitlines()

def avg(input):
    return int(sum(input)/len(input))

input = []
for line in lines:
    for num in line.split(","):
        if(num.isdigit()):
            input.append(int(num))
#part 1
input.sort()
median = int(np.median(input))
fuel=0
for pos in input:
    fuel+=abs(pos-median)

print("input: ",input)
print("median: ",median)
print("part1 solution: ",fuel)

#part 2 (BRUTE FORCE)
def getFuelCost(start,end):
    fuelIncrementer=1
    cost=0
    if(start<end):
        for i in range(start,end):
            cost+=fuelIncrementer
            fuelIncrementer+=1
    else:
        for i in range(end,start):
            cost+=fuelIncrementer
            fuelIncrementer+=1

    return cost


min = 100000000000
for possibleBestLocation in range(np.min(input),np.max(input)):
    sum=0
    for num in input:
        cost = getFuelCost(num,possibleBestLocation)
        sum+=cost
    if(sum < min):
        min = sum
print("part 2 solution: ",min)
