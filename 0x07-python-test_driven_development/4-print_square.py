#!/usr/bin/python3

"""Define a function that prints a square with the character #"""


def print_square(size):
    """
    The print_square() function prints a square with the character #

    Args:
        size(int): Size lenght of square to be printed

    Raises:
        TypeError: If size is not a number(integer)
        ValueError: If size is less than 0
        TypeError: If size is a float and less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")

        print("")