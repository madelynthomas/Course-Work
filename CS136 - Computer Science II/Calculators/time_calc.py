#!/usr/bin/env python

"""

An implemation of a time based function.

"""


def time_calc(secs):
    """Returns a time.

    The function takes secs as a parameter and returns
    the seconds since midnight as hours:minutes:meridian
    in a standard AM/PM time.

    """

    hours = (secs) / (60 * 60) % 12
    minutes = (secs / 60) % 60
    if hours == 0:
        hours == 12
    if secs / (60 * 60) >= 12:
        meridian = " PM"
    else:
        meridian = " AM"
    if minutes < 10:
        minutes = "0" + str(minutes)
    return str(hours) + ":" + str(minutes) + meridian
