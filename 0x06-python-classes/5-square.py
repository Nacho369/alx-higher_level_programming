#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Represents a Square Object"""

    def __init__(self, size=0):
        """Initialize a Square instance

        Args:
            size: Size of the Square Instance
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the Square Object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the Square Object

        Args:
            value: Value of the Square Object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

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

        [print("#" * self.__size) for row in range(self.__size)]
