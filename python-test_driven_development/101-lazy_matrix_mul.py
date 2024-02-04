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
        ValueError: If either m_a or m_b is a string,
        as scalar operands are not allowed; use '*' instead.
    """
    if isinstance(m_a, str):
        raise ValueError("Scalar operands are not allowed; use '*' instead.")
    elif isinstance(m_b, str):
        raise ValueError("Scalar operands are not allowed; use '*' instead.")
    else:
        return np.matmul(m_a, m_b)
