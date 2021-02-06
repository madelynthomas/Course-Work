#!/usr/bin/env python

"""

A function to find the minimum value within a single list.

"""


def find_min(lst):
    minimum = lst[0]
    for value in lst:
        if value < minimum:
            minimum = value
    return minimum
