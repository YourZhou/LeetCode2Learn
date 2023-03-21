def quick_sort(num_list):
    quick_in(num_list, 0, len(num_list) - 1)


def quick_in(num_list, start, end):
    if end > start:
        pv_index = quick_mail(num_list, start, end)
        quick_in(num_list, start, pv_index - 1)
        quick_in(num_list, pv_index + 1, end)
    return num_list


def quick_mail(num_list, start, end):
    pv = num_list[end]
    change = start - 1
    for i in range(start, end):
        if num_list[i] < pv:
            change += 1
            num_list[i], num_list[change] = num_list[change], num_list[i]
    change += 1
    num_list[change], num_list[end] = num_list[end], num_list[change]
    return change


if __name__ == '__main__':
    res = str(input())
    fin_str = []
    buf = ''
    for i in res:
        if i not in buf:
            buf += i
        else:
            fin_str.append(len(buf))
            print(buf)
            buf = ''
            buf += i
    quick_sort(fin_str)
    print(fin_str)
