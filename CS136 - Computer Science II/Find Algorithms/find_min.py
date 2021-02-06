#!/usr/bin/env python

"""

A simple function to the find the minimum value's position.

"""


def find_min(data):
    """Finds the minimum value in a list.

    Args:
        data: A list of integer values

    Returns:
        An integer index in which the smallest value in data is located.
        If the list is empty, this function returns None

    """
    if data == []:
        return None
    pos = 0
    n = len(data)
    smallest = data[0]
    for i in range(1, n):
        if i < smallest:
            smallest = data[i]
            pos = i
    return pos
