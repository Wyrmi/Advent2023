import fileinput
filepath = 'data/13.txt'
sum = 0
listlist = []
listlist.append([])
listlist[0].append([])
x = 0
y = 0
for line in fileinput.input(filepath, inplace = False):
    if line == '\n':
        listlist.append([])
        x = x + 1
        y =0
        listlist[x].append([])
    else:
        for char in line:
            if char != '\n':
                listlist[x][y].append(char)
        y = y + 1
        listlist[x].append([])
#check each block in listlist[] for horizontal and vertical symmetries
#add found symmetries to sum with horizontals multiplied by 100
print(sum)
