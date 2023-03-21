import collections

while True:
    try:
        inStr = str(input())
        dic = collections.OrderedDict()
        for i in inStr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic = sorted(dic.items(), key=lambda k: k[0])
        # print(dic)
        dic = sorted(dic, key=lambda k: k[1], reverse=True)
        # print(dic)
        outStr = ''
        for k, _ in dic:
            outStr += k
        print(outStr)

    except:
        break
