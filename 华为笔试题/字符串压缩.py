num = str(input())
lis = []
buf = 0
n = 0
for i in num:
    if i == buf:
        n += 1
    else:
        if n > 0:
            lis.append(str(n))
        buf = i
        lis.append(buf)
        n = 0
        n += 1
lis.append(str(n))
print(lis)
if len(num) < len(lis):
    print(num)
else:
    fin_s = ""
    for l in lis:
        fin_s+=str(l)
    print(fin_s)
