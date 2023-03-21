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
        inNum = float(input())
        print(inNum)
    except:
        break