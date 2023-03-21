while True:
    try:
        res = str(input())
        res = list(res)
        l = []
        fin_str = ''
        for i in res:
            l.append(res.count(i))
        l.sort()
        small = int(l[0])
        for n in res:
            num = res.count(n)
            if num > small:
                print(n, end='')
    except:
        break
