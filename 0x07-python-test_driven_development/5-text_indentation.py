#!/usr/bin/python3
"""This defines a text-indentation function."""


def text_indentation(text):
    """To only print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    see = 0
    while see < len(text) and text[see] == ' ':
        see += 1

    while see < len(text):
        print(text[see], end="")
        if text[see] == "\n" or text[see] in ".?:":
            if text[see] in ".?:":
                print("\n")
            see += 1
            while see < len(text) and text[see] == ' ':
                see += 1
            continue
        see += 1
