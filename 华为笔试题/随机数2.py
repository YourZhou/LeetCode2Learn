while True:
    try:
        lis=[]
        num = int(input())
        for i in range(num):
            lis.append(int(input()))
        lis.sorted()
        s=set(lis)
        for n in s:
            print(n)
    except:
        break