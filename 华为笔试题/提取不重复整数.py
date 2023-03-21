while True:
    try:
        num = str(input())
        num = num[::-1]
        fin_num = ''
        for i in num:
            if i not in fin_num:
                fin_num += i
        print(fin_num)
    except:
        break
