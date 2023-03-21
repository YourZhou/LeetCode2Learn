while True:
    try:
        res = str(input())
        num = int(input())
        g_num = 0
        c_num = 0
        fin_ratio = 0
        re_str = ''
        for i in range(len(res)-(num-1)):
            s = res[i:i + num]
            for n in s:
                if n == 'G'or n == 'C':
                    g_num += 1
            ratio = g_num / len(res)
            g_num = 0
            # print(ratio)
            if ratio > fin_ratio:
                fin_ratio = ratio
                re_str = s
        print(re_str)
    except:
        break
