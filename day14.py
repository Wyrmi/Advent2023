import fileinput
filepath = 'data/14.txt'
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

#drop Os to north if . on top
for y in range(1, len(listlist)):
    for x in range(len(listlist[y])):
        j = y
        if listlist[y][x] == 'O':
            while listlist[j - 1][x] == '.':
                if j==0:
                    break
                listlist[j][x] ='.'
                j = j - 1
                listlist[j][x] ='O'

#sum up the Os according to vertical position
for y in range(len(listlist)):
    for x in range(len(listlist[y])):
        if listlist[y][x] == 'O':
            sum = sum + (len(listlist)-y)
print(sum)
