#!/usr/bin/python3
"""Fuc defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """To return the product of two matrices.

    Args:
        m_a (list of lists of ints/floats): First matrix.
        m_b (list of lists of ints/floats): Second matrix.
    """

    return (np.matmul(m_a, m_b))
