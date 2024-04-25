import fileinput
import functools
total =0

@functools.cache
def func(row, faults):
    #validation
    if '?' not in row:
        check = row.replace('.', ' ').split()
        if len(check) == len(faults):
            for y in range(len(faults)):
                if len(check[y]) != faults[y]:
                    return 0
            return 1
        return 0
    #recursion
    for x in row:
        if x == '?':
            return func(row.replace("?", ".", 1), faults) + func(row.replace("?", "#", 1), faults)

filepath = 'data/12.txt'
for line in fileinput.input(filepath, inplace = False):
    row = line.split(" ")
    faults = [int(i) for i in row[1].split(",")]
    total += func(row[0],tuple(faults))
print(f"total {total}")