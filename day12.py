import fileinput
import functools
sum =0

@functools.cache
def func(row, faults):
    #validation
    if '?' not in row:
        check = row.replace('.', ' ').split()
        if len(check) == len(faults):
            ok = 1
            for y in range(len(faults)):
                if len(check[y]) != faults[y]:
                    ok = 0
                    break
            global sum
            sum += ok
    else:
        #recursion
        for x in row:
            if x == '?':
                func(row.replace('?', '.', 1),faults)
                func(row.replace('?', '#', 1),faults)

filepath = 'data/12.txt'
for line in fileinput.input(filepath, inplace = False):
    row = line.split(" ")
    faults = [int(i) for i in row[1].split(",")]
    func(row[0],tuple(faults))
print(f"total {sum}")