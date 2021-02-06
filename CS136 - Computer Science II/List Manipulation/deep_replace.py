#!/usr/bin/env python

"""

A deep replace recursive function.

"""


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1:]


def is_list(lst):
    return isinstance(lst, list)


def deep_replace(lst, old, new):
    if not lst:
        return lst
    elif is_list(first(lst)):
        return [deep_replace(first(lst), old, new)] + \
            deep_replace(rest(lst), old, new)
    elif first(lst) == old:
        return [new] + deep_replace(rest(lst), old, new)
    else:
        return [first(lst)] + deep_replace(rest(lst), old, new)
