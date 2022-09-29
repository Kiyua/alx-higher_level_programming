#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [list(map(lambda x: x*x, numbers)) for numbers in matrix]
    return squares
