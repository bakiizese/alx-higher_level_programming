#!/usr/bin/python3
def max_integer(my_list=[]):
    ma = my_list[0]
    ln = len(my_list) - 1
    for i in range(ln):
        if ma < my_list[i]:
            ma = my_list[i]
    return ma
