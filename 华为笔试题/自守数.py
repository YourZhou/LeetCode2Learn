while True:
    try:
        num = int(input())
        n = 0
        for i in range(0,num+1):
            if str(i**2)[(-int(len(str(i)))):] == str(i):
                n+=1
        print(n)
    except:
        break
