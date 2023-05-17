#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = [[j ** 2 for j in i] for i in matrix]
    return n
