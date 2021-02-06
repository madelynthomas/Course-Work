#!/usr/bin/env python

"""

A function adder that adds two lists together and returns one list.

"""


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1:]


def is_list(lst):
    return isinstance(lst, list)


def adder(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    else:
        return [first(lst1) + first(lst2)] + adder(rest(lst1), rest(lst2))
