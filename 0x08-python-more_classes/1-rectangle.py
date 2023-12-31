#!/usr/bin/python3
"""A Rectangle class."""


class Rectangle:
    """A rectangle."""

    def __init__(self, width=0, height=0):
        """To initialize a new Rectangle.

        Args:
            width (int): The new rectangle width.
            height (int): The new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To set/get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To set/get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
