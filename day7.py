import fileinput
filepath = 'data/7.txt'
sum = 0
hicards = []
onepairs = []
twopairs = []
threes = []
fulls = []
fours = []
fives = []

for line in fileinput.input(filepath, inplace = False):
    round = line.split()
    hand = []
    for c in round[0]:
        if c.isdigit():
            hand.append(int(c))
        else:
            match c:
                case 'A':
                    hand.append(14)
                case 'K':
                    hand.append(13)
                case 'Q':
                    hand.append(12)
                case 'J':
                    hand.append(11)
                case 'T':
                    hand.append(10)
    htype = len(set(hand))
    if htype ==1:
        #five of a kind
        fives.append((hand,round[1]))
    elif htype ==2:
        #four of a kind or full house
        my_dict = {i:hand.count(i) for i in hand}
        if 4 in my_dict.values():
             fours.append((hand,round[1]))
        else:
            fulls.append((hand,round[1]))
    elif htype ==3:
        #two pairs or three of a kind
        my_dict = {i:hand.count(i) for i in hand}
        if 3 in my_dict.values():
             threes.append((hand,round[1]))
        else:
            twopairs.append((hand,round[1]))
    elif htype ==4:
        #one pair
        onepairs.append((hand,round[1]))
    elif htype ==5:
        #high card
        hicards.append((hand,round[1]))

hicards.sort()
onepairs.sort()
twopairs.sort()
threes.sort()
fulls.sort()
fours.sort()
fives.sort()

hands = []
hands.extend(hicards)
hands.extend(onepairs)
hands.extend(twopairs)
hands.extend(threes)
hands.extend(fulls)
hands.extend(fours)
hands.extend(fives)

i = 1
for h in hands:
    sum = sum + i * int(h[1])
    i+=1
print(sum)
