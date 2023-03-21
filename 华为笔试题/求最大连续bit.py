while True:
    try:
        num = str(bin(int(input())))
        lis = []
        n = 0
        for i in num:
            if i == '1':
                n += 1
            else:
                lis.append(n)
                n = 0
        lis.append(n)
        print(max(lis))
    except:
        break
