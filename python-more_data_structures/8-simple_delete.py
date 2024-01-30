#!/usr/bin/python3
# a function that deletes a key in a dictionary.
def simple_delete(a_dictionary, key=""):
    keys = a_dictionary.keys()
    if key in keys:
        a_dictionary.pop(key)
    return a_dictionary
