#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ln = len(my_list)
    my_list.reverse()
    for i in range(ln):
        print("{}".format(my_list[i]))
