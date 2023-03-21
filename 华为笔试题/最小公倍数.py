def small2(num1, num2):
    c = num1
    while True:
        if c % num1 == 0 and c % num2 == 0:
            return c
        c += 1


def small(num1, num2):
    for i in range(0, num2 + 1):
        now1 = i * num1
        if now1 % num2 == 0 and now1 != 0:
            return now1


while True:
    try:
        num1, num2 = map(int, input().split())
        now1 = 0
        now2 = 0

        print(small(num1, num2))
    except:
        break
