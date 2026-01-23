#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: Must be an integer or float
        b: Must be an integer or float (default 98)

    Returns:
        The addition of a and b as integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    