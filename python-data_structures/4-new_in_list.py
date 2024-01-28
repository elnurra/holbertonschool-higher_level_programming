#!/usr/bin/python3
"""
Write a function that replaces an element in a list at a specific
position without modifying the original list
"""


def new_in_list(my_list, idx, element):
    copy = my_list[0:]
    count = len(my_list)
    if idx < 0:
        return copy
    elif idx >= count:
        return copy
    else:
        copy[idx] = element
        return copy
