num = int(input())
str_num = str(num)
if str_num[0] == '-':
    str_num = str_num[1:][::-1]
    str_num = '-'+str_num
else:
    str_num = str_num[::-1]
str_num = int(str_num)
if str_num>(-2**31) and str_num<(2**31-1):
    print(str_num)
else:
    print (0)