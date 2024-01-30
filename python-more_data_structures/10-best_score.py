#!/usr/bin/python3
# function that returns a key with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    values = a_dictionary.values()
    max_value = max(values)
    keys = a_dictionary.keys()
    for keys in a_dictionary:
        if a_dictionary[keys] == max_value:
            return keys
