def pp(num):
    drink = 0
    all = float('inf')
    while all >= 2:
        full = num // 3
        drink += full
        ept = num % 3
        all = full + ept
        num = all
        if all == 2:
            drink += 1
            break
    return drink


while True:
    try:
        num = int(input())
        print(pp(num))
    except:
        pass
