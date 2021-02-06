#!/usr/bin/env python

"""

Recursion methods.

"""


def trace(func):
    trace.indent_level = 0

    def ppt(t):
        return ", ".join(str(elem) for elem in list(t))

    def wrapped_call(*args):
        print("|  " * trace.indent_level + "> " + func.__name__
              + "(" + ppt(args) + ")")
        trace.indent_level += 1
        ret = func(*args)
        trace.indent_level -= 1
        print("|  " * trace.indent_level + "< return " + str(ret))
        return ret
    return wrapped_call


def first(lst):
    return lst[0]


def rest(lst):
    return lst[1:]


def is_list(lst):
    return isinstance(lst, list)


def contains(lst, elem):
    if not lst:
        return 0
    else:
        return first(lst) == elem or contains(rest(lst), elem)


def sum(lst):
    if not lst:
        return 0
    else:
        return first(lst) + sum(rest(lst))


def len(lst):
    if not lst:
        return 0
    else:
        return 1 + len(rest(lst))


def average(lst):
    if not lst:
        return 0
    else:
        return average_helper(lst, 0, 0)


def average_helper(lst, sum_so_far, count_so_far):
    if not lst:
        return sum_so_far / count_so_far
    else:
        return average_helper(rest(lst)), sum_so_far \
            + first(lst, count_so_far + 1)


def find_min(lst):
    if not lst:
        return None
    elif not rest(lst):
        return first(lst)
    else:
        min_lower = find_min(rest(lst))
        if min_lower < first(lst):
            return min_lower
        else:
            return first(lst)


def reverse(lst):
    if not lst:
        return lst
    elif is_list(first(lst)):
        return reverse(rest(lst)) + [reverse(first(lst))]
    else:
        return reverse(rest(lst)) + [first(lst)]


def every_other(lst):
    if not lst:
        return lst
    else:
        return [first(lst)] + every_other(rest(rest(lst)))


def all_pairs(lst1, lst2):
    if not lst1 or not lst2:
        return [None]
    else:
        return [first(lst1), first(lst2)] \
            + all_pairs([rest(lst1), (rest(lst2))])


def groupify(lst, size):
    if size == 0:
        return lst
    else:
        return groupify_helper(lst, [], size, 0)


def groupify_helper(lst, sublist_so_far, size, num_so_far):
    if not lst:
        return [sublist_so_far]
    elif size == 0:
        return lst
    elif num_so_far == size:
        return [sublist_so_far] + groupify_helper(lst, [], size, 0)
    else:
        return groupify_helper(
            rest(lst), sublist_so_far + [first(lst)], size, num_so_far + 1)


def merge(lst1, lst2):
    if not lst1:
        return lst2
    elif not lst2:
        return lst1
    else:
        if first(lst1) < first(lst2):
            return [first(lst1)] + merge(rest(lst1), lst2)
        else:
            return [first(lst2)] + merge(lst1, rest(lst2))


def merge_sort(lst):
    if not lst or not rest(lst):
        return lst
    else:
        mid = len(lst) / 2
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


def partion(lst, pivot):
    if not lst:
        return [], [], []
    else:
        left, center, right = partion(rest(lst), pivot)
        if first(lst) < pivot:
            return [first(lst)] + left, center, right
        elif first(lst) == pivot:
            return left, [first(lst)] + center, right
        elif first(lst) > pivot:
            return left, center, [first(lst)] + right


@trace
def recursive_quick_sort(lst):
    if not lst or not rest(lst):
        return lst
    else:
        pivot = first(lst)
        left, center, right = partion(lst, pivot)
        return recursive_quick_sort(left) + center + \
            recursive_quick_sort(right)


print(recursive_quick_sort([5, 2, 42, 12, 52]))
