from collections import defaultdict

num = int(input())
dic = defaultdict(int)
i, j = float('inf'), 0
for _ in range(num):
    start, end = input().split(' ')
    start, end = int(start), int(end)
    i = min(start, i)
    j = max(j, end)
    print(i, j)
    for v in range(start, end + 1):
        dic[v] += 1
print(i, j)
print(dic)
res = 0
for k in range(i, j + 1):
    if dic[k] == 0:
        print("k=0", k)
        res += 1
    elif dic[k] == 1:
        print("k=1", k)
        res += 3
    elif dic[k] > 1:
        print("k>1", k)
        res += 4
print(res)
