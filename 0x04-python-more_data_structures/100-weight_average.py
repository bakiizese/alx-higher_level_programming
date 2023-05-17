#!/usr/bin/python3
def weight_average(my_list=[]):
    result = sum([a[0] * a[1] for a in my_list]) / (sum([a[1] for a in my_list]) or 1)
    return result
