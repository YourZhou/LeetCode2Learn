while True:
    try:
        res1 = str(input())
        res2 = str(input())
        long_res = ''
        short_res = ''
        num = 1

        if len(res1) == len(res2):
            long_res = res1
            short_res = res2
        elif len(res1) > len(res2):
            long_res = res1
            short_res = res2
        else:
            long_res = res2
            short_res = res1
        for i in range(len(short_res)):
            if short_res[i] != long_res[i]:
                # print(long_res[i])
                num += 1
        num+=len(long_res)-len((short_res))
        print("1/%d" % num)
    except:
        break
