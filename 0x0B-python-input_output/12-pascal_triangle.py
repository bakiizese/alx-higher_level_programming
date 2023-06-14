#!/usr/bin/python3
'''triangle function'''


def pascal_triangle(n):
    '''Pascal's Triangle'''
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        tri = tr[-1]
        tm = [1]
        for i in range(len(tri) - 1):
            tm.append(tri[i] + tri[i + 1])
        tm.append(1)
        tr.append(tm)
    return tr
