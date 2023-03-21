while True:
    try:
        num = int(input())
        dic = {}
        for i in range(num):
            index, value = map(int, input().split())
            if index in dic.keys():
                dic[index] += value
            else:
                dic[index] = value
        for n in dic:
            print("%d %d" % (n, dic[n]))
    except:
        break

