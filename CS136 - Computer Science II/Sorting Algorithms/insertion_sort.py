#!/usr/bin/env python

"""

Insertion Sort.

"""

from __future__ import print_function
import random


def insertion_sort(in_values):
    values = list(in_values)
    for i in range(len(values)):
        value = values[i]
        left_pos = i - 1
        while left_pos >= 0 and values[left_pos] > value:
            values[left_pos + 1], values[left_pos] = values[left_pos], value
            left_pos -= 1
    return values


lst = [random.randint(1, 100) for i in range(10)]

print("Insertion Sort List:", (insertion_sort(lst)))
