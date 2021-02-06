#!/usr/bin/env python

"""A function to determine the max grades.


"""


def max_grades(grades):
    maximum = grades[0]
    for grade in grades:
        if grade > maximum:
            maximum = grade
    return maximum
