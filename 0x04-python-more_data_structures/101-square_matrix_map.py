#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    result = [map(lambda a: [map(lambda y: y**2, a)], matrix)]
    return result
