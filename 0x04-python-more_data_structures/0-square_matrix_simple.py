#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for items in matrix:
        squared.append([c**2 for numbers in items])
    return squared
