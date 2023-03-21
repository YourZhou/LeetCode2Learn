def issu(num):
    # 质数大于 1
    if num > 1:
        # 查看因子
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

    # 如果输入的数字小于或等于 1，不是质数
    else:
        return False


while True:
    try:
        inNum = int(input())
        half_inNum = inNum // 2
        buf = 0
        i = 0
        num1 = 3
        while (num1 > 0):
            if half_inNum % 2 == 0:
                num1 = half_inNum - 1 - (i * 2)
            else:
                num1 = half_inNum - (i * 2)
            if issu(num1):
                buf = inNum - num1
                if issu(buf):
                    break
            i += 1
        print(num1)
        print(buf)
    except:
        break
