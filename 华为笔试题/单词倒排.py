while True:
    try:
        res = str(input())
        set_res = ''
        k = False
        for i in res:
            if i.isalpha():
                set_res += i
                k = False
            else:
                if k == False:
                    set_res += ' '
                    k = True
        lis = list(set_res.split(' '))
        lis = lis[::-1]
        fin_set = ''
        for n in lis:
            if len(n) <= 20:
                fin_set += str(n) + ' '
        print(fin_set[:-1])
    except:
        break
