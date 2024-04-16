#!/usr/bin/python3

"""Define is_same_class() function to test if an object is an
instance of a class"""


def is_same_class(obj, a_class):
    """The function checks if the object is exactly an instance
    of the specified class

    Args:
        obj: Object to test
        a_class: Class to compare object to

    Return: True if obj is an instance of a_class otherwise False
    """
    if isinstance(obj, a_class):
        return True

    return False
