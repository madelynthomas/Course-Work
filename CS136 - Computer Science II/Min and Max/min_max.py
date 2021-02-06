#!/usr/bin/env python

"""

A function to find the minimum and maximum value within a single list.

"""


def min_max(lst):
    """Finds the minimum and maximum value of lst.

    Returns a tuple in the form (min, max), where min is the
    smallest value in the unsorted list of integers lst, and
    the max is the largest value in lst.

    """
    minimum = lst[0]
    maximum = lst[0]
    for value in lst:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    return minimum, maximum
