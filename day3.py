with open('Advent2023/data3.txt') as f:
    #ls is filedata with each line as a member in a string list
    ls = f.read().splitlines()
#sum is the sum of all of the number adjacent to a symbol
sum = 0
#l is a line in ls
#y is l's index in ls
for y, l in enumerate(ls):
    #x is used for iterating through each char of a line
    x = 0
    while x < len(l):
        #numlen is used to keep track of multidigit numbers
        numlen = 0
        #when the current char is a number
        if ls[y][x].isdigit():
            #iterate how long the number is
            #the 'x < len(l)' here is used to prevent a index out of range error from occurring on the line's last digit, because there is nothing to its left to be checked
            while x < len(l) and ls[y][x].isdigit():
                numlen += 1
                x += 1
            #once the whole number is parsed, record it as integer to num
            num = int(l[x - numlen : x])
            #check if the number is adjacent to a symbol (anything not a number nor a dot)
            if any(
                c not in "1234567890."
                for i in range(max(0, y - 1), min(len(ls), y + 2))
                for c in ls[i][max(0, x - numlen - 1) : min(len(l), x + 1)]
            ):
                #if yes then add the number to the total sum
                sum += num
        #move on to the next char if the current char isn't a digit
        else:
            x += 1
#part 1 solution
print(sum)

#function for checking for adjacent numbers in part 2
#makes sure that the whole number is accounted for when recording it
def get_num(l, x):
    s = e = x
    while s >= 0 and l[s].isdigit():
        s -= 1
    while e < len(l) and l[e].isdigit():
        e += 1
    return int(l[s + 1 : e])

#reset sum from part 1 so we can use the same variable for the total gear ratio of part 2
sum = 0
#same line iteration as in part 1
for y, l in enumerate(ls):
    #enumerate through every char of every line
    #c is current char and x is its index in the line
    for x, c in enumerate(l):
        #if current char is a * aka a potential gear
        if c == "*":
            #add all adjacent numbers into a list
            s = list(
                {
                    get_num(ls[i], j)
                    for i in range(max(0, y - 1), min(len(ls) + 1, y + 2))
                    for j in range(max(0, x - 1), min(len(l) + 1, x + 2))
                    if ls[i][j].isdigit()
                }
            )
            #if two numbers adjacent to it
            if len(s) == 2:
                #multiply them together and add them to the total sum
                sum += s[0] * s[1]
#part 2 solution
print(sum)
