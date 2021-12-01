file1 = open('input/input1_sample', 'r')
lines = file1.read().splitlines()


intLines= [int(i) for i in lines]
print(lines[1]+lines[2])
print(intLines[1]+intLines[2])