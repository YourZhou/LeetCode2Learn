while True:
    try:
        goal = 0
        res = str(input())
        length = len(res)
        if length <= 4:
            goal += 5
        elif 5 <= length <= 7:
            goal += 10
        else:
            goal += 25
        if res.isalpha():
            if res.isupper() or res.islower():
                goal += 10
            else:
                goal += 20
        n = 0
        s = 0
        f = 0
        b = 0
        for i in range(length):
            if res[i].isdigit():
                n += 1
            elif res[i].isupper():
                s += 1
            elif res[i].islower():
                b += 1
            else:
                f += 1
        if n == 1:
            goal += 10
        elif n > 1:
            goal += 20
        if f == 1:
            goal += 10
        elif f > 1:
            goal += 25

        if n > 0 and (s > 0 or b > 0):
            goal += 2
            if f > 0:
                goal += 1
                if s > 0 and b > 0:
                    goal += 2

        if goal >= 90:
            print("VERY_WEAK")
        elif 80 <= goal <= 90:
            print("WEAK")
        elif 70 <= goal <= 80:
            print("AVERAGE")
        elif 60 <= goal <= 70:
            print("STRONG")
        elif 50 <= goal <= 60:
            print("VERY_STRONG")
        elif 25 <= goal <= 50:
            print("SECURE")
        elif 0 <= goal <= 25:
            print("VERY_SECURE")

    except:
        break
