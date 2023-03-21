def rever(inStr):
    outStr = []
    for i in inStr:
        if i.islower():
            outStr.append(i.upper())
        else:
            outStr.append(i.lower())
    return outStr


while True:
    try:
        reStr = str(input())
        deStr = str(input())
        r2dStr = rever(reStr)
        for i in range(len(r2dStr)):
            if r2dStr[i] == 'Z':
                r2dStr[i] = 'A'
            elif r2dStr[i] == 'z':
                r2dStr[i] = 'a'
            elif r2dStr[i] == '9':
                r2dStr[i] = '0'
            else:
                r2dStr[i] = chr(ord(r2dStr[i]) + 1)
        # print(r2dStr)
        d2rStr = rever(deStr)
        for i in range(len(d2rStr)):
            if d2rStr[i] == 'A':
                d2rStr[i] = 'Z'
            elif d2rStr[i] == 'a':
                d2rStr[i] = 'z'
            elif d2rStr[i] == '0':
                d2rStr[i] = '9'
            else:
                d2rStr[i] = chr(ord(d2rStr[i]) - 1)
        #print(d2rStr)
        out_r2dStr = ''
        out_d2rStr = ''
        for i in r2dStr:
            out_r2dStr += i
        for n in d2rStr:
            out_d2rStr += n
        print(out_r2dStr)
        print(out_d2rStr)
    except:
        break
