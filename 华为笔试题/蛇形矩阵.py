while True:
    try:
        a = int(input())
        sum1 = 0
        count = 0
        for i in range(a):
            count += i
            for j in range(i + 1, a+1):
                sum1 += j
                print(sum1,end= ' ')
            print('')
            sum1 = count
    except:
        break
