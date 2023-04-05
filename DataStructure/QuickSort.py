class QuickSort:
    from typing import List
    from random import shuffle
    def sort(self, nums: List):
        # 为了避免出现耗时的极端情况，先随机打乱
        self.shuffle(nums)
        # 排序整个数组（原地修改）
        self._sort(nums, 0, len(nums) - 1)

    def _sort(self, nums, low, high):
        if low > high:
            return
        # 对 nums[lo..hi] 进行切分
        # 使得 nums[lo..p-1] <= nums[p] < nums[p+1..hi]
        p = self.partition(nums, low, high)

        self._sort(nums, low, p - 1)
        self._sort(nums, p + 1, high)

    def partition(self, nums, low, high):
        privot = nums[low]
        # 关于区间的边界控制需格外小心，稍有不慎就会出错
        # 我这里把 i, j 定义为开区间，同时定义：
        # [lo, i) <= pivot；(j, hi] > pivot
        # 之后都要正确维护这个边界区间的定义
        i = low + 1
        j = high
        while i <= j:
            while i < high and nums[i] <= privot:
                i += 1
                # 此 while 结束时恰好 nums[i] > pivot
            while j > low and nums[j] > privot:
                j -= 1
                # 此 while 结束时恰好 nums[j] <= pivot
            if i >= j:
                break

            # 此时 [lo, i) <= pivot && (j, hi] > pivot
            # 交换 nums[j] 和 nums[i]
            self.swap(nums, i, j)
        self.swap(nums, low, j)
        return j

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def shuffle(self, nums):
        shuffle(nums)



if __name__ == '__main__':
    nums = [1, 34, 5, 6, 7, 89, 3, 2, 4]
    quick_sort = QuickSort()
    quick_sort.sort(nums)
    print(nums)
