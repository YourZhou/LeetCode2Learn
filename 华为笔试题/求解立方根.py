while True:
    try:
        num = float(input())
        num = pow(num,1/3)
        print("%.1f"%num)
    except:
        break
