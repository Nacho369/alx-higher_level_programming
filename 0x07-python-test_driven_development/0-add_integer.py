#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is
    performed.

    Args:
        a(int | float): First value to add
        b(int | float): Second value to add

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    Return:
        The sum of arg @a and @b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
