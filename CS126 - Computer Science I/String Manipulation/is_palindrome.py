#!/usr/bin/env python

"""

A function to determine if the input is a palindrome.

"""


def is_palindrome(lst):
    """Determines if lst is palindromic.

    A palindromic list is one that "reads" as a palindrome, i.e. one that reads
    the same forward and backward.

    Args:
        lst: A list of values of any type

    Returns:
        True if lst is palindromic, False if it is not.

    """
    first = 0
    last = len(lst) - 1
    while first < last:
        if not lst[first] == lst[last]:
            return False
        first += 1
        last -= 1
    return True


print(is_palindrome([1]))
