#!/usr/bin/python3
"""Func that defines an object attribute lookup function."""


def lookup(obj):
    """To return a list of an object's available attributes."""
    return (dir(obj))
