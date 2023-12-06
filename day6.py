from functools import reduce
ways = []
times = [53,71,78,80]
distances = [275,1181,1215,1524]
for x in range(0, 4):
    w =0
    for bp in range(1, times[x]):
        dis = (times[x] - bp) * bp
        if dis > distances[x]:
            w+=1
    ways.append(w)
#ways.remove(0)
sum = reduce(lambda x, y: x*y, ways)
print(sum)
f=0
for bp in range(1, 53717880):
        dis = (53717880 - bp) * bp
        if dis > 275118112151524:
            f+=1
print(f)