while True:
    try:
        _ = int(input())
        money = 100
        for i in range(0, 21):
            for j in range(0, 34):
                if (i * 5) + (j * 3) + (100 - i - j) / 3 == 100:
                    print("%d %d %d" % (i, j, (100 - i - j)))
    except:
        break
