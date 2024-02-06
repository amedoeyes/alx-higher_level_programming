#!/usr/bin/python3

"""pascal triangle"""


def pascal_triangle(n):
    """pascal_triangle"""

    if n <= 0:
        return []

    result = [[1]]
    for i in range(n - 1):
        row = []
        for j in range(i + 2):
            num1 = 0
            num2 = 0

            if j > 0:
                num1 = result[i][j - 1]
            if j < i + 1:
                num2 = result[i][j]

            row.append(num1 + num2)

        result.append(row)

    return result
