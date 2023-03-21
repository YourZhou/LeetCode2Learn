while True:
    try:
        num = int(input())
        lis =[]
        for i in range(num):
            lis.append(str(input()))
        lis.sort()
        for n in lis:
            print(n)
    except:
        break