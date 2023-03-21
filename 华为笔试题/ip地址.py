while True:
    try:
        ip_res = str(input())
        # print(ip_res)
        resend = ''
        for i in ip_res:
            if i == ' ':
                resend = 'NO'
        if resend != 'NO':
            ip_lis = map(int, list(ip_res.split('.')))
            s = 0
            for n in ip_lis:
                if n >= 0 and n <= 255:
                    s = 1
                else:
                    s = 2
                    break
            if s == 1:
                resend = 'YES'
            else:
                resend = 'NO'
        print(resend)
    except:
        break
