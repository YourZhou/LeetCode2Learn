while True:
    try:
        num = int(input())
        all_name = []
        for q in range(num):
            all_name.append(list(str(input()).lower()))

        for name in all_name:
            len_dic = []
            s_n1 = []
            s_n2 = []
            n = 0
            for i in name:
                if i not in s_n1:
                    s_n1.append(i)
            for n in range(len(s_n1)):
                len_dic.append(name.count(s_n1[n]))
            len_dic.sort(reverse=True)
            num1 = 0
            bt = 26
            for j in len_dic:
                num1+=j*bt
                bt-=1
            print(num1)
    except:
        break