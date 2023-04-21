from collections import defaultdict

nums = int(input())
dic = defaultdict(list)
node = list(map(int, input().split(" ")))
print(node)
for i in range(nums):
    dic[node[i]].append(i)
print(dic)
dic = dict(sorted(dic.items(), key=lambda x: -len(x[1])))
print(dic)
res = []
for k in dic.keys():
    if k != -1:
        res.append(k)
print(res)
for i in range(nums):
    if i not in res:
        res.append(i)
print(res)
res = list(map(str,res))
print(" ".join(res))
