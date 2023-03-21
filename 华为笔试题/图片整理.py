while True:
    try:
        res = str(input())
        big_s = []
        small_s = []
        num = []
        fin_str = ''
        for i in res:
            if i.isupper():
                big_s.append(i)
            elif i.islower():
                small_s.append(i)
            elif i.isdigit():
                num.append(i)

        big_s.sort()
        small_s.sort()
        num.sort()
        for n in num:
            fin_str += n
        for j in big_s:
            fin_str += j
        for k in small_s:
            fin_str += k
        print(fin_str)

    except:
        break
