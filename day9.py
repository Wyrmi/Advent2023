import fileinput
from itertools import pairwise
filepath = 'Advent2023/data9.txt'
sum = 0
for line in fileinput.input(filepath, inplace = False):
    numbers = []
    for x in line.split():
        if x.isdigit():
            numbers.append(int(x))
        elif x.lstrip('-').isdigit():
            numbers.append(-1 * int(x.lstrip('-')))
    bool = True
    numbers.reverse() #comment this out for p1
    ls = numbers
    ite = []
    while(bool):
        lis = []
        for x in range(0, len(ls)-1):
            lis.append(ls[x +1 ] - ls[x])
        bool = any(lis)
        ite.append(lis[-1])
        ls = lis
    ite.reverse()
    tmp = 0
    for x in ite:
        tmp = tmp + x
    tmp = tmp + numbers[-1]
    sum = sum + tmp 
print(sum)
