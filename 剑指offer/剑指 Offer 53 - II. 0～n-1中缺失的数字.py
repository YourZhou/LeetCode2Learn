from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        times = 0
        for i in nums:
            if not times == i:
                return times
            else:
                times += 1
        return nums[-1]+1


if __name__ == '__main__':
    s = "abcdefg"
    solution = Solution()
    print(solution.reverseLeftWords(s, 2))
