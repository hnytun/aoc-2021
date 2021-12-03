from collections import Counter
file1 = open('input/input3_Sample', 'r')

lines = file1.read().splitlines()
lines2 = lines.copy()

def GetGamma(list,epsilon):
    lineLength = len(list[0])
    result=""
    currentIndex=0
    for i in range(0,lineLength):
        ones=0
        zeroes=0
        for line in list:
            if(line[i]) in "1":
                ones+=1
            else:
                zeroes+=1
        if(ones>zeroes):
            result+="1"
        elif(zeroes>ones):
            result+="0"
        else:
            if(not epsilon):
                result+="1"
            else:
                result+="0"
    if(not epsilon):
        return result
    else:
        return ''.join('1' if x == '0' else '0' for x in result)

print(GetGamma(lines,True)) #gamma
print(GetGamma(lines,False)) #epsilon


while(len(lines)!=1):
    for j in range(0,5):
        for line in lines:
            if(line[j] != GetGamma(lines,False)[j]):
                lines.remove(line)

while(len(lines2)!=1):
    for j in range(0,5):
        print("most common on index " + str(j) +" is " + GetGamma(lines,False)[j])
        for line in lines2:
            print(lines2)
            if(line[j] == GetGamma(lines,False)[j]):
                lines2.remove(line)
