#!/usr/bin/python3
# function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    dic_keys = sorted(list(a_dictionary))
    for i in dic_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
