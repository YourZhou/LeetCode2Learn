def isok(inStr1, inStr2):
    for i in inStr1:
        if i not in inStr2:
            return 'false'
    return 'true'


while True:
    try:
        inStr1 = str(input())
        inStr2 = str(input())
        print(isok(inStr1,inStr2))
    except:
        break
