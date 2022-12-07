#!/usr/bin/env python3
"""
排序：
1.冒泡排序bubble sort、选择排序、插入排序
2.快速排序、堆排序、归并排序
3.希尔排序、计数排序、基数排序
"""
import random


# v1 升序排列
def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:  # if li[j] < li[j + 1]: 降序排列
                li[j], li[j + 1] = li[j + 1], li[j]


li = [random.randint(0, 10000) for i in range(1000)]
print(li)
bubble_sort(li)
print(li)


# v2 打印排序过程
def bubble_sort2(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:  # if li[j] < li[j + 1]: 降序排列
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)


li = [3, 2, 6, 23, 89, 3, 1]
bubble_sort2(li)


# v3 升序排列改进 加入标志位
def bubble_sort3(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:  # if li[j] < li[j + 1]: 降序排列
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


li = [9, 8, 7, 1, 2, 3, 4, 5]
bubble_sort3(li)
