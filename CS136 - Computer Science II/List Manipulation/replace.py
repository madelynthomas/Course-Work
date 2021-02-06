#!/usr/bin/env python

"""

Replace function.

"""


def replace(lst, old, new):
    """
    Creates a copy of lst, but with all occurrences of
    old replaced by new
    """
    new_lst = []
    for elem in lst:
        if elem == old:
            new_lst.append(new)
        else:
            new_lst.append(elem)
    return new_lst
