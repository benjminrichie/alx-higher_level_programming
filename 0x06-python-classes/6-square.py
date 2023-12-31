#!/usr/bin/python3
"""This will define a class Square."""


class Square:
    """This will represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """To initialize a new square.
        Args:
            size (int): Represents the
            size of the new square.
            position (int, int): The position
            of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """To set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """To set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Just return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """To print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for code in range(0, self.__position[1])]
        for code in range(0, self.__size):
            [print(" ", end="") for jeh in range(0, self.__position[0])]
            [print("#", end="") for keh in range(0, self.__size)]
            print("")
