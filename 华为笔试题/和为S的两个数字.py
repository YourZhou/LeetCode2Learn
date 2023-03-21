while True:
    try:
        in_lis = list(map(int, input().split()))
        s = int(input())
        all_lis = []
        for i in in_lis:
            if s - i in in_lis:
                all_lis.append([i, int(s - i)])
        fin_lis = []
        buf = 0
        for n in all_lis:
            print(n)
            if n[0] * n[1] > buf:
                buf = n[0] * n[1]
                fin_lis = n
        print(fin_lis)
    except:
        break
