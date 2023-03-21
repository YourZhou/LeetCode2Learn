if __name__ == '__main__':
    in_num = list(map(int, input().split()))
    print('*****************\n' + str(in_num) + '\n*****************')
    all_num = 0
    lis = []
    for i in range(in_num[0], in_num[1] + 1):
        n = i
        if i == in_num[2]:
            all_num += 1
        else:
            while n >= 10:
                if n // 10 == in_num[2] or n % 10 == in_num[2]:
                    all_num += 1
                    print(i)
                    break
                else:
                    n = n // 10
    # all_num += 1
    # lis[] = i //
    # if i//1 or :
    #     all_num += 1
    # num = in_num[2]
    # i = 1
    # j = 0
    # while num <= in_num[1]:
    #     j = num * i
    #     i += 1
    #     all_num+=1
    # for n in range(1,in_num[1]+1):
    #     for j in range(n):
    #         print(str(in_num[2]),end='')
    #     print('')
    print('***************\n' + str((in_num[1] - in_num[0] - all_num+1)) + '\n*****************')
