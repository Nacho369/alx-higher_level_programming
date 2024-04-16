#!/usr/bin/python3

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represent a BaseGeometry class"""
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value passed

        Args:
            name(str): String value
            value(int): Value to validate

        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
