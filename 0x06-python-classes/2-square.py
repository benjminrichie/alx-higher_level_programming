#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """This will represent a square."""

    def __init__(self, size=0):
        """To initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        self.__size = size
