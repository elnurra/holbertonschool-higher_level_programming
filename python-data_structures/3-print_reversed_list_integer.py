#!/usr/bin/python3
# Write a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    new_list = my_list[::-1]
    for i in new_list:
        print("{:d}".format(i))
