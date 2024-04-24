import fileinput
import sys
filepath = 'data/2.txt'
red = 12
green = 13
blue = 14
bool = False
isok = False
sum = 0
for line in fileinput.input(filepath, inplace = False):
    isok = True
    words = line.split()
    for w in words:
        if w.isdigit():
            bool = True
            num = int(w)
        elif bool:
            if w[0] == "b":
                if num > 14:
                    isok = False
            elif w[0] == "g":
                if num > 13:
                    isok = False
            elif w[0] == "r":
                if num > 12:
                    isok = False
            bool = False
    if isok:
        sys.stdout.write(words[1] + ' ok\n')
        sum = sum + int(words[1].strip(":"))
sys.stdout.write('sum is ' + str(sum))

