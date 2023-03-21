while True:
    try:
        n , k = map(int,input().split())
        lis = list(map(int,input().split()))
        lis.sort()
        fin_str = ''
        for i in range(k):
            fin_str+=str(lis[i])
            fin_str+=' '
        print(fin_str[:-1])
    except:
        break