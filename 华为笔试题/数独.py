while True:
    try:
        inLis = []
        for i in range(9):
            inLis.append(list(map(int, input().split())))
        print(inLis)
    except:
        break
