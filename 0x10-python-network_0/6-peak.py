#!/usr/bin/python3
"""An algorithm for list of integers."""


def find_peak(list_of_integers):
    """To find peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
