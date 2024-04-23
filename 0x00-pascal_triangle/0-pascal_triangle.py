#!/usr/bin/python3
"""Module to find Pascal's Triangle integers"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle up to the nth row.
            Each inner list corresponds to a row in the triangle.

        If n is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
    return triangle
