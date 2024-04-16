#!/usr/bin/python3

"""Defines is_kind_of_class() function"""


def is_kind_of_class(obj, a_class):
    """The function checks if the object is an instance of, or if
    the object is an instance of a class that inherited from, the
    specified class

    Args:
        obj: Object to check
        a_class: Tyoe to compare to

    Return: True if obj is an instance of or if obj is an instance
            of a class that inherited from the specified class,
            otherwise False
    """
    if isinstance(obj, a_class):
        return (True)

    return (False)
