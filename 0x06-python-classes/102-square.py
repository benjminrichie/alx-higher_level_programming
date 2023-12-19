#!/usr/bin/python3
"""This will define a class Square."""


class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """Will initializes a new square.
        Args:
            size (int): Tp represent the
            size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """To returns the current size of the square.........."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Only returns the current area of the square........."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """This defines the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """This defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """This defines the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """This defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """This defines the > comparison to a Square......."""
        return self.area() > other.area()

    def __ge__(self, other):
        """This defines the >= comparison to a Square.........."""
        return self.area() >= other.area()
