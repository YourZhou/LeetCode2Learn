while True:
    try:
        res = str(input())
        lis = list(res)
        s = 0
        for n in res:
            if res.count(n)==1:
                s = 1
                print(n)
        if s == 0:
            print('-1')
    except:
        break
