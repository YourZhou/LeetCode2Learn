def isok(inStr):
    if len(inStr) <= 8:
        return "NG"
    buf = []
    for i in range(3, len(inStr) // 2 + 1):
        for j in range(len(inStr)):
            if j + i > len(inStr):
                break
            if inStr[j:j + i] in buf:
                return "NG"
            buf.append(inStr[j:j + i])
            print(buf)
        buf = []

    sata = [0, 0, 0, 0]
    for i in inStr:
        # print(i)
        if i.islower():
            sata[0] = 1
        elif i.isupper():
            sata[1] = 1
        elif i.isdigit():
            sata[2] = 1
        else:
            sata[3] = 1
        # print(sata)
    # print(sum(sata))
    if sum(sata) >= 3:
        return "OK"
    else:
        return "NG"


while True:
    try:
        inStr = str(input())
        print(inStr)
        print(isok(inStr))

    except:
        break
