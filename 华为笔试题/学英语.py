def num2str(num):
    m1 = ' ,one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen'.split(
        ',')
    m2 = ' , ,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')
    if num < 20:
        return m1[num]
    if num >= 20:
        s = m2[num // 10]
        if num % 10 != 0:
            s = s + ' ' + m1[num % 10]
        return s


while True:
    try:
        inNum = int(input())
        print("input num = " + str(inNum))
        print(num2str(20))
        outStr = ""
        if inNum >= 1000000:
            if inNum // 1000000 >= 100:
                outStr += (num2str(inNum // 1000000 // 100) + ' ' + 'hundred' + ' ' + 'and' + ' ')
            outStr += (num2str(inNum // 1000000 % 100) + ' ' + 'million' + ' ')
        inNum %= 1000000
        if inNum >= 1000:
            if inNum // 1000 >= 100:
                outStr += (num2str(inNum // 1000 // 100) + ' ' + 'hundred' + ' ' + 'and' + ' ')
            outStr += (num2str(inNum // 1000 % 100) + ' ' + 'thousand' + ' ')
        inNum %= 1000
        if inNum >= 100:
            outStr += (num2str(inNum // 100) + ' ' + 'hundred' + ' ' + 'and' + ' ')
        outStr += (num2str(inNum % 100) + ' ')
        print(outStr)

    except:
        break
