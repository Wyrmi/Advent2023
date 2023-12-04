import fileinput
filepath = 'Advent2023/data4.txt'
sum = 0
winnums = []
nums = []
samenums = []
for line in fileinput.input(filepath, inplace = False):
    sline=line.rstrip().split("|")
    for x in sline[0].split():
        if x.isdigit():
            winnums.append(int(x))
    for x in sline[1].split():
        nums.append(int(x))
    samenums = set(winnums).intersection(nums)
    if samenums:
        sum = sum + 2 ** (len(samenums)-1)
    winnums.clear()
    nums.clear()
    samenums.clear()
print(sum)