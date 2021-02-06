#!/usr/bin/env python

"""

Fibonacci number in recursion and non-recursion.

"""


def trace(func):
    trace.indent_level = 0

    def ppt(t):
        return ", ".join(str(elem) for elem in list(t))

    def wrapped_call(*args):
        print("|  " * trace.indent_level + "> " +
              func.__name__ + "(" + ppt(args) + ")")
        trace.indent_level += 1
        ret = func(*args)
        trace.indent_level -= 1
        print("|  " * trace.indent_level + "< return " + str(ret))
        return ret
    return wrapped_call

# Recursion


@trace
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Non-Recursion; memoization
stash = {}


def fib_memo(n):
    if n < 3:
        return 1
    else:
        if n in stash:
            return stash[n]
        else:
            stash[n] = fib_memo(n - 1) + fib_memo(n - 2)
            return stash[n]


print(fib(9))
