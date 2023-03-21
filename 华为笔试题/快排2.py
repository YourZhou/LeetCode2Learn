def quick_sort(num_list):
    qucik_in(num_list, 0, len(num_list) - 1)


def qucik_in(num_list, start, end):
    if end > start:
        pv_index = quick_mail(num_list, start, end)
        qucik_in(num_list, start, pv_index - 1)
        qucik_in(num_list, pv_index + 1, end)
    return num_list


def quick_mail(num_list, start, end):
    pv = num_list[end]
    change = start - 1
    for n in range(start, end):
        if num_list[n] < pv:
            change += 1
            num_list[n], num_list[change] = num_list[change], num_list[n]
    change += 1
    num_list[change], num_list[end] = num_list[end], num_list[change]
    return change


def bubble(num_list):
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list

def merge_sort(arr):
    """归并排序"""
    if len(arr) == 1:
        return arr
    # 使用二分法将数列分两个
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 使用递归运算
    return marge(merge_sort(left), merge_sort(right))


def marge(left, right):
    """排序合并两个数列"""
    result = []
    # 两个数列都有值
    while len(left) > 0 and len(right) > 0:
        # 左右两个数列第一个最小放前面
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # 只有一个数列中还有值，直接添加
    result += left
    result += right
    return result

# merge_sort([11, 99, 33 , 69, 77, 88, 55, 11, 33, 36,39, 66, 44, 22])

# 返回结果[11, 11, 22, 33, 33, 36, 39, 44, 55, 66, 69, 77, 88, 99]

if __name__ == '__main__':
    lis = [0, 2, 3, 4, 1, 6, 3, 2, 4, 89, 4, 0, 2, 3, 60, 2, 3, 4, 1, 6, 3, 2, 4, 89, 4, 0, 2, 3, 6]
    fin_lis = merge_sort(lis)
    print(fin_lis)
