#!/usr/bin/python3
"""This only defines a class Square."""


class Square:
    """This represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """This initializes a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): This is the position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """To return the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("This size must be an integer")
        elif value < 0:
            raise ValueError
        self.__size = value

    @property
    def position(self):
        """This will return the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(code, int) for code in value) or
                not all(code >= 0 for code in value)):
            raise TypeError("This position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """This only eturns the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Will print a square using the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for tit in range(0, self.__position[1])]
        for tit in range(0, self.__size):
            [print(" ", end="") for jeh in range(0, self.__position[0])]
            [print("#", end="") for keh in range(0, self.__size)]
            print("")

    def __str__(self):
        """This only define print() representation of a Square."""
        if self.__size != 0:
            [print("") for tit in range(0, self.__position[1])]
        for tit in range(0, self.__size):
            [print(" ", end="") for jeh in range(0, self.__position[0])]
            [print("#", end="") for keh in range(0, self.__size)]
            if tit != self.__size - 1:
                print("")
        return ("")
