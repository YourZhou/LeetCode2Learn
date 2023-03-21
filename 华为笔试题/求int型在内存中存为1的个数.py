while True:
    try:
        num = str(bin(int(input(),10)))
        n = 0
        for i in num:
            if i == '1':
                n+=1
        print(n)
    except:
        break