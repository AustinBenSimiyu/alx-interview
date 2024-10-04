#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.

The function `pascal_triangle(n)` returns a list of lists representing
the Pascal's triangle of size `n`.
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of size n."""
    if n <= 0:
        return []
    triangle = [[1]]  # Start with the first row
    for i in range(1, n):
        prev_row = triangle[-1]
        # Generate the next row by
        # adding adjacent elements from the previous row
        row = [1]  # First element is always 1
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)  # Last element is always 1
        triangle.append(row)
    return triangle
