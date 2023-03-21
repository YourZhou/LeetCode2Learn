target = int(input())
i, j, res = 1, 2, []
while j <= (target // 2 + 1):
    count_sum = sum(list(range(i, j + 1)))
    if count_sum > target:
        i += 1
    elif count_sum < target:
        j += 1
    else:
        res.append(list(range(i, j + 1)))
        i += 1
print(res)
