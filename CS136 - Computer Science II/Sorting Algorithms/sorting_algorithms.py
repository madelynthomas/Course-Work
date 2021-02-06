#!/usr/bin/env python

"""

Selection Sort and Insertion Sort Algorithms.

"""

import random


def selection_sort(data):
    print("Original:", data)
    comps = 0
    swaps = 0
    values = list(data)
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(values)):
            comps += 1
            if values[j] < values[min_index]:
                min_index = j
        if i != min_index:
            values[i], values[min_index] = values[min_index], values[i]
            swaps += 2
    print("Sorted List:", values)
    print("Comparisions:", comps)
    print("Swaps:", swaps)
    return values


def insertion_sort(data):
    print("Original:", data)
    comps = 0
    swaps = 0
    values = list(data)
    for i in range(len(data)):
        value = values[i]
        left_pos = i - 1
        while left_pos >= 0 and values[left_pos] > value:
            comps += 1
            values[left_pos + 1] = values[left_pos]
            swaps += 1
            left_pos -= 1
        if left_pos + 1 != i:
            swaps += 1
            values[left_pos + 1] = value
        if left_pos >= 0:
            swaps += 1
    print("Sorted List:", values)
    print("Comparsions:", comps)
    print("Swaps:", swaps)
    return values


lst = [random.randint(1, 100) for i in range(10)]
print("Selection Sort:"), selection_sort(lst)
print()
print("Insertion Sort:"), insertion_sort(lst)
