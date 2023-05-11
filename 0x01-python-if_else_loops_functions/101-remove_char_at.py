#!/usr/bin/python3
def remove_char_at(str, n):
    k = ''
    j = 0
    for i in str:
        if j != n:
            k += str[j]
        j += 1
    return k
