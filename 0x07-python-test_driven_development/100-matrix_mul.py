#!/usr/bin/python3

"""Defines matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if any(type(num) not in [int, float] for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if any(type(num) not in [int, float] for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]
