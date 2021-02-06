#!/usr/bin/env python

"""

Recursive Quick-Sort

"""


def recursive_quick_sort(lst):
    left = []
    pivot_lst = []
    right = []
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        for i in lst:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                pivot_lst.append(i)
        left = recursive_quick_sort(left)
        right = recursive_quick_sort(right)
        return left + pivot_lst + right


print recursive_quick_sort([2, 56, 1, 5, 0, 12, 43, 21])
