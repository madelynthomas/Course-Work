#!/usr/bin/env python

"""

An implementation of the linear search as well as finding the position.

"""


def linear_search(data, item):
    for elem in data:
        if elem == item:
            return True
        else:
            return False


def linear_search_position(data, item):
    for i, elem in enumerate(data):
        if elem == item:
            return True, i
        else:
            return False, None
