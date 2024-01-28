#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.
def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        return None
    else:
        my_list.sort()
        return my_list[-1]
