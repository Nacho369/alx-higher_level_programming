#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Represents a Square Object"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance

        Args:
            size: Size of the Square Instance
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the current size of the Square Object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the Square Object

        Args:
            value: Value of the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the current position of the Square Object"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the current size of the Square Object

        Args:
            value: Value of the position
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(val >= 0 for val in value) or
                not all(isinstance(val, int) for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the Area of the square

        Return: Current Square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in the stdout with the character #
        """
        if (self.__size == 0):
            print("")

        [print("") for x in range(self.__position[1])]
        [print(" " * self.__position[0] + "#" * self.__size)
            for row in range(self.__size)]
