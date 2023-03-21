import collections

while True:
    try:
        inNum = int(input())
        if int(input()) == 0:
            reser = True
        else:
            reser = False
        # print(reser)
        dic = collections.OrderedDict()
        for i in range(inNum):
            inName, inGoal = str(input()).split(' ')
            dic[inName] = int(inGoal)
            # print(dic)
        dic = sorted(dic.items(), key=lambda k: k[1], reverse=reser)
        # print(dic)
        for k, v in dic:
            print(k, v)

    except:
        break
