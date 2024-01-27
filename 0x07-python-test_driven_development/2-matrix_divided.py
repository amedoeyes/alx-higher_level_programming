#!/usr/bin/python3

"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix by a number
    Args:
        matrix: list of lists of integers or floats
        div: number to divide the matrix by
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    Returns: new matrix with all elements divided by div
    """

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(type(row) is list for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(type(num) in [int, float] for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
