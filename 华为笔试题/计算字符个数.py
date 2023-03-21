while True:
    try:
        res = str(input())
        lis = []
        for i in res:
            lis.append(i)
        A = str(input())
        num1 = lis.count(A.lower())
        num2 = lis.count(A.upper())
        print(num1+num2)
    except:
        break