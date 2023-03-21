# -*- coding: UTF-8 -*-
# 十大经典排序算法

from random import randint
from time import process_time

nums_lists = [[] for n in range(4)]
for n in range(500):
    nums_lists[0].append(randint(-400, 400))
for n in range(1000):
    nums_lists[1].append(randint(-8000, 8000))
for n in range(5001):
    nums_lists[2].append(randint(-2000, 2000))
for n in range(10000):
    nums_lists[3].append(randint(-9000, 9000))


# 冒泡排序
def bubble_sort(num_list):
    for n in range(len(num_list) - 1):
        for m in range(len(num_list) - 1 - n):
            if num_list[m] > num_list[m + 1]:
                num_list[m + 1], num_list[m] = num_list[m], num_list[m + 1]
    return num_list


# 快速排序
# def quick_sort(num_list):
#     quick_recursion(num_list, 0, len(num_list) - 1)
#
#
# def quick_recursion(num_list, head_index, tail_index):
#     if head_index < tail_index:
#         piovt_index = quick_partition(num_list, head_index, tail_index)
#         quick_recursion(num_list, head_index, piovt_index - 1)
#         quick_recursion(num_list, piovt_index + 1, tail_index)
#     return num_list
#
#
# def quick_partition(num_list, head_index, tail_index):
#     pivot = num_list[tail_index]
#     exchange_index = head_index - 1
#     for n in range(head_index, tail_index):
#         if num_list[n] < pivot:
#             exchange_index += 1
#             num_list[exchange_index], num_list[n] = num_list[n], num_list[exchange_index]
#     num_list[exchange_index + 1], num_list[tail_index] = num_list[tail_index], num_list[exchange_index + 1]
#     return exchange_index + 1

def quick_sort(num_list):
    qucik_in(num_list, 0, len(num_list) - 1)


def qucik_in(num_list, start, end):
    if end > start:
        pv_index = quick_mail(num_list, start, end)
        qucik_in(num_list, start, pv_index - 1)
        qucik_in(num_list, pv_index + 1, end)
    return num_list


def quick_mail(num_list, start, end):
    pv = num_list[end]
    change = -1
    for n in range(start, end):
        if num_list[n] < pv:
            change += 1
            num_list[n], num_list[change] = num_list[change], num_list[n]
    change += 1
    num_list[change], num_list[end] = num_list[end], num_list[change]
    return change
