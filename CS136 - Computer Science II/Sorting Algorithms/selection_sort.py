#!/usr/bin/env python

"""

Selection Sort.

"""

import random


def selection_sort(in_values):
    values = list(in_values)
    for i in range(len(values)):
        min_index = i
        for j in range(i, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
    return values


lst = [random.randint(1, 100) for i in range(10)]

print("Original List:", (lst))
print("Selection Sort List:", (selection_sort(lst)))
