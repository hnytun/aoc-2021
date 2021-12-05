from collections import Counter
file1 = open('input/input3', 'r')

lines = file1.read().splitlines()
lines2 = lines.copy()

def GetGamma(list):
    lineLength = len(list[0])
    result=""
    currentIndex=0
    for i in range(0,lineLength):
        ones=0
        zeroes=0
        for line in list:
            if(line[i] in "1"):
                ones+=1
            else:
                zeroes+=1
        if(ones>zeroes):
            result+="1"
        elif(zeroes>ones):
            result+="0"
        else:
            result+="1"
    return result

def GetEpsilon(list):

    lineLength = len(list[0])
    result=""
    currentIndex=0
    for i in range(0,lineLength):
        ones=0
        zeroes=0
        for line in list:
            if(line[i] in "1"):
                ones+=1
            else:
                zeroes+=1
        if(ones>zeroes):
            result+="0"
        elif(zeroes>ones):
            result+="1"
        else:
            result+="0"
    return result #01010

for j in range(0,12):
    lines[:] = [x for x in lines if x[j] == GetGamma(lines)[j]]

for i in range(0,12):
    lines2[:] = [x for x in lines2 if x[i] == GetEpsilon(lines2)[i]]
    if(len(lines2) == 1 ):
        break

print(int(lines[0],2)*int(lines2[0],2))





#print(lines2)
#print(GetGamma(["00100", "11110", "10110", "11111"]))
#print(GetEpsilon(["00100", "11110", "10110", "11111"]))

