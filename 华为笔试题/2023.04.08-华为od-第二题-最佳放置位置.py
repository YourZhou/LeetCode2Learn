homes = int(5)
longStr = "0 20 40 10 30".split(" ")
longs = []
for i in longStr:
    longs.append(int(i))
n = 0
sums = 0
res = float('inf')
for i in range(max(longs)):
    sums = 0
    for j in longs:
        sums += abs(j - i)
    if sums < res:
        res = sums
        n = i
print(n)
