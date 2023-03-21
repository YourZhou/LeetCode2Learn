while True:
    try:
        res = str(input())
        lis_res = list(res)
        lis_res.sort()
        s = set(lis_res)
        print(s)
        num_dic = {}
        for i in s:
            num_dic[i] = res.count(i)
        print(max(num_dic))
        fin_lis = []

        # print(lis_res)
    except:
        break
