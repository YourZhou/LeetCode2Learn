while True:
    try:
        s_num = int(input())
        l_num = s_num ** 3
        lis = {}
        sum = 0
        n = 1
        while sum < l_num:
            sum = 0
            for i in range(s_num):
                num = n + 2 * i
                lis[i] = num
                sum += num
            n += 2
        fin_str = ''
        for n in lis:
            fin_str += str(lis[int(n)])
            fin_str += '+'
        print(fin_str[:-1])
    except:
        break
