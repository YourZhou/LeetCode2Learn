from typing import List


def binary_search(nums: List[int], target: int):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return False


def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 判断 target 是否存在于 nums 中
    # 此时 target 比所有数都大，返回 -1
    if left == len(nums):
        return -1
    # 判断一下 nums[left] 是不是 target
    return left if nums[left] == target else -1

def right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 此时 left - 1 索引越界
    if left - 1 < 0:
        return -1
    # 判断一下 nums[left] 是不是 target
    return left - 1 if nums[left - 1] == target else -1
