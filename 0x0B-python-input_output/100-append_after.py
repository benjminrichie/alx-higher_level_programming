#!/usr/bin/python3
"""func defines a text file insertion"""


def append_after(filename="", search_string="", new_string=""):
    """to insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for myLines in r:
            text += myLines
            if search_string in myLines:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
