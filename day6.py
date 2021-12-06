
file1 = open('input/input6', 'r')
lines = file1.read().splitlines()

fishes = []
for line in lines:
    for num in line.split(","):
        if(num.isdigit()):
            fishes.append(int(num))

def shiftAll(cycle):

    temp=cycle.copy()

    cycle[8] = temp[0]
    cycle[7] = temp[8]
    cycle[6] = temp[7]
    cycle[6] += temp[0]
    cycle[5] = temp[6]
    cycle[4] = temp[5]
    cycle[3] = temp[4]
    cycle[2] = temp[3]
    cycle[1] = temp[2]
    cycle[0] = temp[1]
    return cycle


def countFishes(existingFishes,days):
    sum=len(existingFishes)
    cycle = [0,0,0,0,0,0,0,0,0]
    #add existing fish to cycle
    for i in existingFishes:
        cycle[i]+=1

    #for each day
    for day in range(0,days):
        sum += cycle[0]
        cycle = shiftAll(cycle).copy()
    return sum


print("part 1 (after 80 days): ",countFishes(fishes,80))
print("part 2 (after 256 days): ",countFishes(fishes,256))












#print(len(fishes))
