#!/usr/bin/env python

"""

A function to find the maximum value within a single list.

"""


def find_max(lst):
    maximum = lst[0]
    for value in lst:
        if value > maximum:
            maximum = value
    return maximum


print("Maximum Value in Lst:", find_max([1, 2, 3, 8, 5, 6]))
