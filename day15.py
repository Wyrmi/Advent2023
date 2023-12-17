import fileinput
filepath = 'Advent2023/data15.txt'
sum = 0
tsum = 0
sline = []
for line in fileinput.input(filepath, inplace = False):
    sline.extend(line.rstrip().split(","))

for x in sline:
        sum = 0
        for char in x:
            sum = sum + ord(char)
            sum = sum * 17
            sum = sum % 256
        tsum = tsum + sum
       
print(tsum)