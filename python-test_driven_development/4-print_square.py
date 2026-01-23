#!/usr/bin/python3
"""
Module that prints a square using # characters.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: Size of the square (must be integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is negative
    """
    # Check if size is a negative float first
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
