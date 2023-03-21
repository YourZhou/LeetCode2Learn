res = []
res.append(input())
res.append(input())
for i in res:
    while len(i) > 8:
        print(i[:8])
        i = i[8:]
    if len(i) < 8:
        for n in range(8 - len(i)):
            i += '0'
        print(i)
