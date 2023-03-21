from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        r = []
        for i in nums:
            if not i in r:
                r.append(i)
            else:
                return i
        return None
