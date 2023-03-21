while True:
    try:
        inNum = int(input())
        sums = 0
        buf_lis = []
        for i in range(1,inNum):
            # print(i)
            for j in range(1,i):
                if i % j == 0:
                    buf_lis.append(j)
            # print(buf_lis)
            buf_sum = sum(buf_lis)
            # for n in buf_lis:
            #     buf_sum+=n
            if buf_sum == i:
                sums+=1
            # print(sums)
            buf_lis = []
        print(sums)

    except:
        break
