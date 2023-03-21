from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        times = nums.count(target)
        return times


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    solution = Solution()
    print(solution.search(nums,target))
