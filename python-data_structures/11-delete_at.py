#!/usr/bin/python3
# Write a function that deletes the item at a specific position in a list
def delete_at(my_list=[], idx=0):
    count = len(my_list)
    if idx >= count or idx < 0:
        return my_list
    else:
        del my_list[idx]
        return my_list
