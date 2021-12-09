file1 = open('input/input8_sample', 'r')
lines = file1.read().split("\n")
"""
input=list()
for line in lines:
    input.append(line.strip().replace("|",""))
"""
input=list()

for line in lines:
    split = line.split(" | ")
    input.append(split[0])
    input.append(split[1])

def IsValid(potensialCombo,validCombos):
    validCombos = validCombos.split(" ")
    for valid in validCombos:
        if(sorted(potensialCombo) == sorted(valid)):
            return True
    return False

def Decode(signal):
    signal = ''.join(sorted(signal))
    if(len(signal) == 2):
        return 1
    elif(len(signal) == 4):
        return 4
    elif(len(signal) == 3):
        return 7
    elif(len(signal) == 7):
        return 8
    else:
        return 404

def DecodePart2(signals):
    decoded=dict()
    for signal in signals:
        if(len(signal) == 2):
            decoded["1"] = signal
            return 1
        elif(len(signal) == 4):
            decoded["4"] = signal
            return 4
        elif(len(signal) == 3):
            decoded["7"] = signal
            return 7
        elif(len(signal) == 7):
            decoded["8"] = signal
            return 8
    return decoded



pairs = [(i,j) for i,j in zip(input[::2], input[1::2])]
"""
occurrences=[0,0,0,0,0,0,0,0,0,0]
#part 1
for pair in pairs:
    for output in pair[1].split(" "):
        if(IsValid(output,pair[0])):
            decoded=Decode(output)
            if(decoded!=404):
                occurrences[decoded]+=1
sum=0
for i in range(0,len(occurrences)):
    sum+=occurrences[i]
print("part 1: ", sum)
"""


#part 2:
for pair in pairs:
    split = pair[1].split(" ")
    print(split)









