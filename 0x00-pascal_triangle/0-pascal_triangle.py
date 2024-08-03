#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    Args:
    n (int): The number of rows of Pascal's Triangle to generate.
    Returns:
    List[List[int]]: A list of lists where each list represents a row of Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

