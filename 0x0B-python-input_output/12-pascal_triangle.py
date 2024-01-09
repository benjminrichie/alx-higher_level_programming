#!/usr/bin/python3
"""func that defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """simply represent Pascal's Triangle of size n.

    only returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for eye in range(len(tri) - 1):
            tmp.append(tri[eye] + tri[eye + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
