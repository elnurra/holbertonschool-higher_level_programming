#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (numpy.ndarray or str): The first matrix.
        m_b (numpy.ndarray or str): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.

    Raises:
        ValueError: If either m_a or m_b is a string, as matrix multiplication is not defined for strings.
    """
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise ValueError("Matrix multiplication is not defined for a string.")
    else:
        return np.matmul(m_a, m_b)

