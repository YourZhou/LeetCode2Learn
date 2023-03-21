while True:
    try:
        num = int(input())
        lis = list(map(int, input().split()))
        k = int(input())
        if k > 0:
            lis = lis[::-1]
            print(lis[k - 1])
        else:
            print(0)
    except:
        break
