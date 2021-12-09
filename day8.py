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

def DecodePart2(signals,validCombos):


    signals = sorted(signals,key=len)
    #print(signals)
    decoded={}
    #set the ones we know from length
    for signal in signals:

        if(IsValid(signal,validCombos) == False):
           continue
        if(len(signal) == 2):
            decoded["1"] = signal
        elif(len(signal) == 4):
            decoded["4"] = signal
        elif(len(signal) == 3):
            decoded["7"] = signal
        elif(len(signal) == 7):
            decoded["8"] = signal






        #if its 3, 5 or 2
        if(len(signal) == 5):

            if("1" in decoded and len(list(set(decoded["1"])&set(signal))) == 2):
                decoded["3"] = signal
            #elif("6" in decoded and len(list(set(decoded["6"])&set(signal))) == 5):
            #    decoded["3"] = signal
            elif("4" in decoded and len(list(set(decoded["4"])&set(signal))) == 3):
                decoded["5"] = signal
            else:
                decoded["2"] = signal

        if(len(signal) == 6):
            if("1" in decoded and len(list(set(decoded["1"])&set(signal))) == 1):
                decoded["6"] = signal
            elif("4" in decoded and len(list(set(decoded["4"])&set(signal))) == 4):
                decoded["9"] = signal
            elif("8" in decoded and len(list(set(decoded["8"])&set(signal))) == 5):
                decoded["9"] = signal
            else:
                decoded["0"] = signal





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
    print(DecodePart2(pair[1].split(" "),pair[0]))


"""
length 2 -> 1

length 3 -> 7

length 4 -> 4

length 5 ->

if 2 letters match with 1 it's 3,

else if 3 letters match with 4 it's 5,

else it's 2

length 6 ->

if 1 letter matches with 1 it's 6

else if 4 letters match with 4 it's 9

else it's 0

length 7 -> 8
"""
