from collections import defaultdict
import heapq

class Solution:

    def open(self, nums, nodes):
        return


cacheSpace, numURL = map(int, input().split(' '))
# cacheSpace, numURL = 2, 5
# print(cacheSpace, numURL)

urlInputs = list(map(int, input().split(' ')))
# urlInputs = [3, 1, 2, 1, 2]
# print(urlInputs)

setUrlTlsNums = int(input())
# setUrlTlsNums = 2
# print(setUrlTlsNums)

urlSet = set(urlInputs)
urlTtlDic = defaultdict(int)
for i in range(setUrlTlsNums):
    urlname, urlttl = map(int, input().split(' '))
    urlTtlDic[urlname] = urlttl
for i in urlSet:
    if urlTtlDic[i] == 0:
        urlTtlDic[i] = 5

# print(urlTtlDic)

res = []
cacheDic = {}
cacheQueue = []

# for inUrl in urlInputs:
#

for inUrl in urlInputs:
    removeKeys = []
    for k, v in cacheDic.items():
        cacheDic[k] -= 1
        if cacheDic[k] == 0:
            removeKeys.append(k)
    for r in removeKeys:
        cacheDic.pop(r)
    if inUrl not in cacheDic.keys():
        if len(cacheDic) == cacheSpace:
            values = cacheDic.values()
            minValue = min(values)
            minKey = None
            for k, v in cacheDic.items():
                if v == minValue:
                    # print(k, v)
                    minKey = k
                    break
            cacheDic.pop(minKey)
        res.append(1)
        cacheDic[inUrl] = urlTtlDic[inUrl]
    else:
        res.append(0)
# print(res)
print(" ".join(list(map(str, res))))
solution = Solution()
# print(solution.open(nums, node))
