def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后


def quick_zhou(arr, start, end):
    if start >= end:
        return
    mid = arr[end]
    L = start
    R = end - 1
    while L < R:
        while L < R and arr[R] >= mid:
            R -= 1
        while L < R and arr[L] <= mid:
            L += 1
        buf = arr[R]
        arr[R] = arr[L]
        arr[L] = buf
    buf = arr[L]
    arr[L] = mid
    mid = buf
    quick_zhou(arr, start, L - 1)
    quick_zhou(arr, R + 1, end)


while True:
    try:
        param = int(input())
        lis = []
        for i in range(param):
            lis.append(int(input()))
        s = set(lis)
        fin_lis = list(s)
        quick_sort(fin_lis, 0, len(fin_lis) - 1)
        for n in fin_lis:
            print(n)
    except:
        break
