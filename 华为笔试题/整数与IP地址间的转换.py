while True:
    try:
        inIP = list(input().split('.'))
        inNum = bin(int(input()))[2:]

        # print(inIP)
        for i in range(len(inIP)):
            inIP[i] = bin(int(inIP[i]))[2:]
            inIP[i] = '0' * (8 - len(inIP[i])) + inIP[i]
            # print(inIP[i])
        bufNum = '0b'
        for i in inIP:
            bufNum += i
        # print(bufNum)
        print(eval(bufNum))

        # print(inNum)
        inNum = '0' * (32 - len(inNum)) + inNum
        # print(inNum)
        bufIP = [inNum[:8], inNum[8:16], inNum[16:24], inNum[24:32]]
        # for i in range(len(bufIP)):
        #     bufIP[i] = '0b'+bufIP[i]
        # print(bufIP)

        # print(bufIP)
        outIP = ''
        for i in range(len(bufIP)):
            # print(outIP)
            outIP += (str(eval('0b' + str(bufIP[i]))) + '.')
        print(outIP[:-1])




    except:
        break
