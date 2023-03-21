while True:
    try:
        res = str(input())
        fin_res = ''
        last_num = False
        for i in range(len(res)):
            if res[i].isdigit():
                if last_num == False:
                    fin_res += '*'
                    last_num = True
            elif not res[i].isdigit():
                if last_num == True:
                    fin_res += '*'
                last_num = False
            fin_res += res[i]
        if fin_res[len(fin_res) - 1].isdigit():
            fin_res += '*'
        print(fin_res)
    except:
        break
