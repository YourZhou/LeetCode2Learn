def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def seclection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


def quick_sort(arr, low, high):
    i = low
    j = high
    if i >= j:
        return arr
    temp = arr[low]
    while i < j:
        while i < j and arr[j] >= temp:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= temp:
            i += 1
        arr[j] = arr[i]
    arr[i] = temp
    quick_sort(arr, low, i - 1)
    quick_sort(arr, i + 1, high)
    return arr


def marge(left, right):
    """排序合并两个数列"""
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append((left.pop(0)))
    result += left
    result += right
    return result


def marge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return marge(marge_sort(left), marge_sort(right))


if __name__ == '__main__':
    lis = [0, 2, 3, 4, 1, 2]
    lis = marge_sort(lis)
    print(lis)
