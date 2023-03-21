while True:
    try:
        res_1 = str(input())
        res_2 = str(input())
        long_res = ''
        short_res = ''
        fin_str = ''
        if len(res_1) >= len(res_2):
            long_res = res_1
            short_res = res_2
        else:
            long_res = res_2
            short_res = res_1
        for i in range(len(short_res)):
            for j in range(i+1,len(short_res)+1):
                # print(short_res[i:j])
                if short_res[i:j] in long_res:
                    if len(short_res[i:j])>len(fin_str):
                        fin_str = short_res[i:j]
        print(fin_str)
    except:
        break
