file1 = open('input/input8_sample', 'r')
lines = file1.read().split("\n")

input=list()
for line in lines:
    input.append(line.strip().replace("|",""))


map = dict()

"""
map["abcefg"] = 0
map["ccff"] = 1
map["acdeg"] = 2
map["acdfg"] = 3
map["bcdf"] = 4
map["abdfg"] = 5
map["abdefg"] = 6
map["acf"] = 7
map["abcdefg"] = 8
map["abcdfg"] = 9
"""


def IsValid(potensialCombo,validCombos):
    validCombos = validCombos.split(" ")
    for valid in validCombos:
        if(sorted(potensialCombo) == sorted(valid)):
            return True
    return False


pairs = list()
for i in range(0,len(input)):
    if(i==19):
        break
    pairs.append((input[i],input[i+1]))
    i=i+2
    print(i)





#print(IsValid("jfke","abcd ekfj jsueh"))


for pair in pairs:
    print(pair[0])
    for output in pair[1].split(" "):
        print(output)
