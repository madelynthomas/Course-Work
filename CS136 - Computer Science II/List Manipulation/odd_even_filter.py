#!/usr/bin/env python

"""

A filter function that seperates odds and evens.

"""


def odd_even_filter(numbers):
    odd_lst = []
    even_lst = []
    for number in numbers:
        if number % 2 == 0:
            even_lst.append(number)
        else:
            odd_lst.append(number)
    return [even_lst], [odd_lst]
