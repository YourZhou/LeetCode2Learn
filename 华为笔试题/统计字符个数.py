while True:
    try:
        res = str(input())
        en = 0
        k = 0
        n = 0
        f = 0
        for i in res:
            if i.isalpha():
                en += 1
            elif i.isdigit():
                n += 1
            elif i == ' ':
                k += 1
            else:
                f += 1
        print(en)
        print(k)
        print(n)
        print(f)
    except:
        break
