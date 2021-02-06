#!/usr/bin/env python

"""

Iterative and non-iterative factorial, Greatest Common Divisor, Ackerman.

"""


def iterative_factorial(n):
    if n <= 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return (factorial)


def factorial(n):
    if n <= 1:
        return 1
    else:
        return (n * factorial(n - 1))


def gcd(a, b):
    c = a % b
    if c == 0:
        return b
    else:
        return (gcd(b, c))


def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return (ack(m - 1, 1))
    else:
        return (ack(m - 1, ack(m, n - 1)))
