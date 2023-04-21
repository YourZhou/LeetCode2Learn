s,n = str(input()).split(" ")
sl = list(s)
n = int(n)
dp = [""] * n
for i in range(len(sl)):
    if (i // n) % 2 == 0:
        dp[i % n] += sl[i]
    else:
        dp[n - 1 - (i % n)] += sl[i]
for j in dp:
    print(j)