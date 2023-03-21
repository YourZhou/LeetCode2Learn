def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j].upper() > arr[j + 1].upper():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


while True:
    try:
        inlis = list(str(input()))
        buf_lis = []
        for i in inlis:
            if i.isalpha():
                buf_lis.append(i)
        # print(buf_lis)
        bubbleSort(buf_lis)
        # print(buf_lis)
        outStr = ""
        for i in range(len(inlis)):
            if inlis[i].isalpha() == False:
                outStr += inlis[i]
                # print(inlis[i], end='')
            else:
                outStr += buf_lis.pop(0)
                # print(buf_lis.pop(0), end='')
        print(outStr)
    except:
        break
