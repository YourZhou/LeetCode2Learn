while True:
    try:
        res = str(input())
        fin_res = ''
        for i in res:
            if i.isupper():
                ac = ord(i)
                if ac == 90:
                    ac = 96
                change = str(chr(ac + 1)).lower()
                fin_res += change
            elif i.islower():
                if i >= 'a' and i <= 'c':
                    fin_res += '2'
                if i >= 'd' and i <= 'f':
                    fin_res += '3'
                if i >= 'g' and i <= 'i':
                    fin_res += '4'
                if i >= 'j' and i <= 'l':
                    fin_res += '5'
                if i >= 'm' and i <= 'o':
                    fin_res += '6'
                if i >= 'p' and i <= 's':
                    fin_res += '7'
                if i >= 't' and i <= 'v':
                    fin_res += '8'
                if i >= 'w' and i <= 'z':
                    fin_res += '9'
            elif i.isdigit:
                fin_res += i

        print(fin_res)
    except:
        break
