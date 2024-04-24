import fileinput
import sys
filepath = 'data1.txt'
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
sys.stdout.write("\n")

sum = 0
nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','1','2','3','4','5','6','7','8','9']
for line in fileinput.input(filepath, inplace = False):
    res = [line[i: j] for i in range(len(line))
          for j in range(i + 1, len(line) + 1)]
    numbers = []
    for r in res:
        if r in nums:
            numbers.append(r)
    i =0
    for n in numbers:
        match n:
            case 'one':
                numbers[i]=1
            case 'two':
                numbers[i]=2
            case 'three':
                numbers[i]=3
            case 'four':
                numbers[i]=4
            case 'five':
                numbers[i]=5
            case 'six':
                numbers[i]=6
            case 'seven':
                numbers[i]=7
            case 'eight':
                numbers[i]=8
            case 'nine':
                numbers[i]=9
            case _:
                pass
        i += 1
    newnum = str(numbers[0]) + str(numbers[-1])
    sum = sum + int(newnum)
sys.stdout.write("sum is ")
sys.stdout.write(str(sum))