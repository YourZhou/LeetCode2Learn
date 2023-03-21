while True:
    try:
        num1 = int(input())
        lis1 = list(map(int,input().split()))[0:num1]
        num2 = int(input())
        lis2 = list(map(int, input().split()))[0:num2]
        all_lis = list(set(lis1 + lis2))

        fin_str = ''
        for i in all_lis:
            fin_str+=str(i)
        print(fin_str)
        # print(all_lis)
    except:
        break

