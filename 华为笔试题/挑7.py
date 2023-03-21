while True:
    try:
        num = int(input())
        lis = []
        for i in range(1, num + 1):
            if i % 7 == 0:
                lis.append(i)
            if '7' in str(i):
                lis.append(i)
        s = set(lis)
        print(len(s))
    except:
        break
