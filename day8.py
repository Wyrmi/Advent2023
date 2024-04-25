import fileinput
filepath = 'data/8.txt'
directions = "LRRLRRRLRRLLLRLLRRLRRLLRRRLRRLLRLRRRLRLRRLRLRRRLRLRLRRLLRLRLRRLRRRLRRRLRRRLRLRRLLLLRLLRLLRRLRRRLLLRLRRRLRLRRRLRLRRLRRRLRRRLRLRLLRRRLLRLLRLRLRLRLLRRLRRLRRRLRRLRLRLRLRLRRLRRRLLRRRLLRLLLRRRLLRRRLRRRLRRLRLRRLRLLRRLLRRLRLRLRRLRLRRLLRRRLLRRRLLRLRRRLRLRRRLRLRRRLRRRLRRLRRLRRLLRRRLRRRLLLRRRR"
dirs = []
for d in directions:
    if d == 'L':
        dirs.append(0)
    else:
        dirs.append(1)
nodes = {}
for line in fileinput.input(filepath, inplace = False):
    node = line.split(" = ")

    nodes[node[0]] = (node[1][1]+node[1][2]+node[1][3],node[1][6]+node[1][7]+node[1][8])

key = 'AAA'
i = 0
steps = 0

while key != 'ZZZ':
    key = nodes[key][dirs[i]]
    steps +=1
    i +=1
    if i == len(dirs):
        i = 0
print(steps)
