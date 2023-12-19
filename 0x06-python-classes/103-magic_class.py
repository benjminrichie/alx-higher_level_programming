#!/usr/bin/python3
"""we define a MagicClass matching exactly a bytecode provided by Holberton."""

from math import *


class MagicClass:
    """This represents a circle."""

    def __init__(self, radius=0):
        """This initializes a MagicClass.
        Arg:
        radius (float or int): New magicClass radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This will return area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """To return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
