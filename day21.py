import fileinput
filepath = 'data/21.txt'
sum = 0
listlist = []
i = 0

#parse puzzle input into a 2d list
for line in fileinput.input(filepath, inplace = False):
    listlist.append([])
    for char in line:
        if char != '\n':
            listlist[i].append(char)
    i = i + 1

for i in range(0,64):
    if i % 2 == 0:
        s = 'S'
        o = 'O'
    else:
        s = 'O'
        o = 'S'
    for y in range(0, len(listlist)):
        for x in range(0, len(listlist[y])):
            if listlist[y][x] == s:
                if y != 0 and listlist[y - 1][x] == '.':
                    listlist[y - 1][x] = o
                if y < len(listlist) -1 and listlist[y + 1][x] == '.':
                    listlist[y + 1][x] = o
                if x != 0 and listlist[y][x -1] == '.':
                    listlist[y][x -1] = o
                if x < len(listlist[y]) -1 and listlist[y][x +1] == '.':
                    listlist[y][x +1] = o
                listlist[y][x] ='.'


for y in range(1, len(listlist)):
        for x in range(len(listlist[y])):
            if listlist[y][x] == s or listlist[y][x] == o:
                sum = sum +1
    
print(sum)