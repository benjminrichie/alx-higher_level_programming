#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for items in range(len(matrix)):
        new_matrix[items] = list(map(lambda x: x**2, matrix[items]))

    return (new_matrix)
