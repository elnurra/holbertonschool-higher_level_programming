#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    count = len(matrix)
    new_list = []
    for i in range(0, count):
        rows = list(map(lambda x: x ** 2, matrix[i]))
        new_list.append(rows)
    return new_list
