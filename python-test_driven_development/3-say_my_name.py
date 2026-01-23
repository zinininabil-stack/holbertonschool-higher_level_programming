#!/usr/bin/python3
"""
Module that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name: First name (must be string)
        last_name: Last name (must be string, optional)

    Raises:
        TypeError: If first_name or last_name is not a string
    """

    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
