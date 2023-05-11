#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if b > a:
        j = add(a, b)
        for i in range(4, 6):
            j = add(j, i)
        return j
    else:
        return sub(a, b)
