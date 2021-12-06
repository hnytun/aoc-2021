
file1 = open('input/input6_sample', 'r')

lines = file1.read().splitlines()

input=[]
for line in lines:
    for num in line.split(","):
        if(num.isdigit()):
            input.append(num)
print(input)
