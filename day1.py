import fileinput
import sys
filepath = 'Advent2023/data1.txt'
newnum = 'test'
sum = 0
for line in fileinput.input(filepath, inplace = False):
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(int(char))
    newnum = str(numbers[0]) + str(numbers[-1])
    sum = sum + int(newnum)
sys.stdout.write("sum is ")
sys.stdout.write(str(sum))
