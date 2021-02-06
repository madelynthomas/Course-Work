#!/usr/bin/env python

"""

A function pairs that returns all the pairs from two lists.

"""

from __future__ import print_function


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1:]


def is_list(lst):
    return isinstance(lst, list)


def pairs(elem, lst):
    if not elem or not lst:
        return lst
    elif is_list(first(lst)):
        return pairs(elem, first(lst)) + pairs(elem, rest(lst))
    else:
        return [[elem, first(lst)]] + pairs(elem, rest(lst))
