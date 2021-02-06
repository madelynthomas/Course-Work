#!/usr/bin/env python

"""

A function flatten that returns one list from two lists.

"""


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1:]


def is_list(lst):
    return isinstance(lst, list)


def flatten(lst):
    if not lst:
        return lst
    elif is_list(first(lst)):
        return flatten(first(lst)) + flatten(rest(lst))
    else:
        return [first(lst)] + flatten(rest(lst))
