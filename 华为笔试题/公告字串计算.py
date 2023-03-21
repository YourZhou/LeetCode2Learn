while True:
    try:
        res1, res2 = (input().split())
        lis = []
        for i in range(len(res1)):
            for j in range(i, len(res1)):
                s = res1[i:j+1]
                if s in res2:
                    lis.append(len(s))
        print(max(lis))



    except:
        break
