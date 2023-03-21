while True:
    try:
        res ,num= input().split()
        num = int(num)
        if res[num - 1].isalpha():
            print(res[:num])
        else:
            print(res[:num-1])
    except:
        break
