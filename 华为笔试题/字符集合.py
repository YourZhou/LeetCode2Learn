while True:
    try:
        inStr = str(input())
        outStr = ""
        for i in inStr:
            if i not in outStr:
                outStr+=i
        print(outStr)
    except:
        break