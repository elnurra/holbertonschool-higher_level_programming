#!/usr/bin/python3
# function that returns the weighted average
# of all integers tuple (<score>, <weight>)
def weight_average(my_list=[]):
    count = len(my_list)
    if count == 0:
        return 0
    sum = 0
    weighted_sum = 0
    for rows in my_list:
        multiply = 1
        for i in rows:
            multiply *= i
        sum += multiply
    for i in range(0, count):
        weighted_sum += my_list[i][1]
    w_average = sum / weighted_sum
    return w_average
