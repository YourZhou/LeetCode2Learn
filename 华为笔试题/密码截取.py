while True:
    try:
        res = str(input())
        length = []
        for i in range(len(res) - 2):
            for j in range(i, len(res) - 2):
                s = res[i:j + 3]
                s1 = s[::-1]
                if s1 == s:
                    length.append(len(s))
        print(max(length))
    except:
        break
