#!/usr/bin/env python

"""

An implementation of merge.

"""


def merge(first, second):
    """Merges two sorted lists while preserving relative ordering.

    To preserve the relative ordering of elements means that if the two lists
    being merged are sorted, the result of merging them is also sorted. See
    the examples. Make sure to leave the argument lists unmodified.

    Args:
        first: A sorted list of integers
        second: A sorted list of integers

    Returns:
        A list that represents the merger of first and second

    """
    new_lst = list()
    first_lst = 0
    second_lst = 0

    while first_lst < len(first) and second_lst < len(second):
        if first[first_lst] < second[second_lst]:
            new_lst.append(first[first_lst])
            first_lst += 1
        else:
            new_lst.append(second[second_lst])
            second_lst += 1

    while first_lst < len(first):
        new_lst.append(first[first_lst])
        first_lst += 1

    while second_lst < len(second):
        new_lst.append(second[second_lst])
        second_lst += 1

    return new_lst


def merge_sort(lst):
    """Utilizes merge method to merge a list sorting it.

    Split the collection into smaller groups by halving it until
    the groups only have one element or no elements. Then merge
    the groups back together so that their elements are in order.

    Args:
        lst: Data to be sorted

    Returns:
        A list recursively sorted using merge_sort and merge

    """
    if len(list) <= 1:
        return lst

    middle = len(lst) / 2
    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))
