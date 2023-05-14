#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    rel = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            rel.append(True)
        else:
            rel.append(False)
    return rel
