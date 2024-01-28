#!/usr/bin/python3
"""
Write a function that returns a tuple with the length of
a string and its first character
"""


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        count = len(sentence)
        char = sentence[0]
        tup = (count, char)
        return tup
