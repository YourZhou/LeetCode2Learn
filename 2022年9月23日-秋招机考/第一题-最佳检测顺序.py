class Solution:
    def __init__(self):
        self.cnt = []
        self.dic = {}

    def open(self, nums, nodes):
        from collections import defaultdict

        self.cnt = [0] * nums
        dic = defaultdict(list)
        for i in range(nums):
            dic[nodes[i]].append(i)
        self.dic = dic
        res = []
        for i in range(nums):
            if self.cnt[i] == 0:
                self.backtrack(i)
            res.append((i, self.cnt[i]))
        res.sort(key=lambda x: (-x[1], x[0]))
        return " ".join(list(map(str, [x[0] for x in res])))

    def backtrack(self, node):
        self.cnt[node] += 1
        for v in self.dic[node]:
            self.backtrack(v)
            self.cnt[node] += self.cnt[v]


if __name__ == '__main__':
    # nums = 5
    # node = [-1, -1, 1, 2, 3]
    nums = int(input())
    node = list(map(int,input().split(' ')))
    solution = Solution()
    print(solution.open(nums, node))
