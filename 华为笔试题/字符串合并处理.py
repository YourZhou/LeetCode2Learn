while True:
    try:
        inStr1, inStr2 = str(input()).split()
        inStr = inStr1 + inStr2
        #print('')
        #print(inStr)
        bufStr1 = []
        bufStr2 = []
        for i in range(len(inStr)):
            if i % 2 == 0:
                bufStr1.append(inStr[i])
            else:
                bufStr2.append(inStr[i])
        #print(bufStr1, bufStr2)
        bufStr1.sort()
        bufStr2.sort()
        #print(bufStr1, bufStr2)
        outStr = ''
        for i in range(len(bufStr1)):
            if '0' <= bufStr1[i] <= '9' or 'a' <= bufStr1[i] <= 'f' or 'A' <= bufStr1[i] <= 'F':
                # bufStr1[i] = str(hex(eval('0b' + str(bin(eval('0x0' + bufStr1[i])))[2:][::-1])))[2:]
                bufStr1[i] = str(bin(eval('0x0' + bufStr1[i])))[2:]
                if len(bufStr1[i]) < 4:
                    for j in range(4 - len(bufStr1[i])):
                        bufStr1[i] = '0' + bufStr1[i]
                bufStr1[i] = str(hex(eval('0b' +bufStr1[i][::-1])))[2:]
            if bufStr1[i].isalpha():
                bufStr1[i] = bufStr1[i].upper()
            outStr += bufStr1[i]
        for i in range(len(bufStr2)):
            if '0' <= bufStr2[i] <= '9' or 'a' <= bufStr2[i] <= 'f' or 'A' <= bufStr2[i] <= 'F':
                # bufStr2[i] = str(hex(eval('0b' + str(bin(eval('0x0' + bufStr2[i])))[2:][::-1])))[2:]
                bufStr2[i] = str(bin(eval('0x0' + bufStr2[i])))[2:]
                if len(bufStr2[i]) < 4:
                    for j in range(4 - len(bufStr2[i])):
                        bufStr2[i] = '0' + bufStr2[i]
                bufStr2[i] = str(hex(eval('0b' + bufStr2[i][::-1])))[2:]
            if bufStr2[i].islower():
                bufStr2[i] = bufStr2[i].upper()
            outStr += bufStr2[i]
        print(outStr)
    except:
        break
