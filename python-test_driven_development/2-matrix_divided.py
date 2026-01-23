#!/usr/bin/python3
"""
Module for matrix division.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: List of lists containing integers or floats
        div: Number (int or float) to divide by

    Returns:
        New matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """

    # Check if division by zero - division by 0 is mathematically impossible
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check div type - must be a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that matrix is a non-empty list
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check that each row of the matrix is a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        # Check that each element in each row is a number
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of "
                    "lists) of integers/floats")

    # Check that all rows have the same number of elements
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

    # Create a new matrix by dividing each element by div
    new_matrix = list(map(lambda row: list(
        map(lambda x: round(x / div, 2), row)), matrix))

    return (new_matrix)
