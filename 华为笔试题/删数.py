while True:
    try:
        inNum = int(input())
        if inNum > 1000:
            inNum = 1000
        arr = [1 for i in range(inNum)]
        # print(arr)
        i = 0
        path = 0
        two = 1
        while 1 in arr:
            if two == 3:
                arr[i] = 0
                two = 0
                path = i
                # print(arr)
            if i == len(arr) - 1:
                i = 0
            else:
                i += 1
            if arr[i] != 0:
                two += 1
        print(path)

    except:
        break
