num1 = input().split('.')
num2 = input().split('.')
mask = input().split('.')
res1 = ''
res2 = ''
res_mask = ''
for i in num1:
    res1 += str(bin(int(i))[2:].zfill(8))
for n in num2:
    res2 += str(bin(int(n))[2:].zfill(8))
for j in mask:
    res_mask += str(bin(int(j))[2:].zfill(8))

if int(res1) & int(res_mask) == int(res2) & int(res_mask):
    print("1 " + str(int(res1) & int(res_mask)))
else:
    print("0 " + str(int(res1) & int(res_mask)))
