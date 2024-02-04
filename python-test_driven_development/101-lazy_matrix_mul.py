#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices using numpy"""

    return (np.matmul(m_a, m_b))
