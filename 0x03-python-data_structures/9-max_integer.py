#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if my_list != 0:
        ma = my_list[0]
        for i in range(ln):
            if ma < my_list[i]:
                ma = my_list[i]
        return ma
    else:
        return "None"
