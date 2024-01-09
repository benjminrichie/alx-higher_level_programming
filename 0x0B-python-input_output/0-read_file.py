#!/usr/bin/python3
"""The func that defines a text file-reading"""


def read_file(filename=""):
    """To print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
