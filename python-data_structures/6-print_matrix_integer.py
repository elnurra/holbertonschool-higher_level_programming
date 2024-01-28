#!/usr/bin/python3
# Write a function that prints a matrix of integers.
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for members in row:
            if row.index(members) == len(row) - 1:
                print(members, end="")
            else:
                print("{:d}".format(members), end=" ")
        print()
