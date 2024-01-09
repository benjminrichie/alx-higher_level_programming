#!/usr/bin/python3
"""this defines a Python class-to-JSON function."""


def class_to_json(obj):
    """to return the dictionary represntation of a simple data structure."""
    return obj.__dict__
