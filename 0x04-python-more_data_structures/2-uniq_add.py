#!/usr/bin/python3
def uniq_add(my_list=[]):
    newset = set(my_list)
    sums = 0
    for i in newset:
        sums += i
    return sums
