while True:
    try:
        inStr = str(input())
        raStr = str(input())
        stata = 'true'
        i = 0
        j = 0
        while j != len(raStr) - 1:
            print(inStr[i])
            print(raStr[j])
            if (inStr[i] == '?'):
                i += 1
                j += 1
                continue
            elif (inStr[i] == '*'):
                i += 1
                j += 1
                if (inStr[i] == '?'):
                    i += 1
                try:
                    while (inStr[i] != raStr[j]):
                        j += 1
                except:
                    stata = 'false'
                    break
                continue
            elif (inStr[i] != raStr[j]):
                stata = 'false'
                break
            i += 1
            j += 1
        print(stata)
    except:
        break
