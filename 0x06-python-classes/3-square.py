#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Represents a Square Object"""

    def __init__(self, size=0):
        """Initialize a Square instance

        Args:
            size: Size of the Square Instance
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the Area of the square

        Return: Current Square area
        """
        return (self.__size * self.__size)
