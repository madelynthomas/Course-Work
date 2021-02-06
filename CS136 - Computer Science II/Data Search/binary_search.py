#!/usr/bin/env python

"""

An implementation of binary search.

"""


def binary_search(data, item):
    low = 0
    high = len(data) - 1
    while low <= high:
        middle = (low + high) / 2
        value = data[middle]
        if value == item:
            return True
        elif value < item:
            low = middle + 1
        elif value > item:
            high = middle - 1
    return False
