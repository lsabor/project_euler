# This module holds basic matrix functions

import numpy as np


def parse_mat_string(mat_string):
    # parses matrix from specific string notation
    if mat_string[0] == "0":  # fixes leading 0 issue
        mat_string == " " + mat_string
    mat_string = mat_string.replace("\n", "; ")
    mat_string = mat_string.replace(" 0", " ")
    matrix = np.matrix(mat_string)
    return matrix


def get_std_diagonals(matrix):
    # gets diagonals from a matrix top left to bottom right
    diags = []
    n = matrix.shape[0]
    for i in range(n):
        diags.append(matrix.diagonal(i, 0, 1))
        if i:
            diags.append(matrix.diagonal(i, 1, 0))
    return diags


def get_all_diagonals(matrix):
    # gets all diagonals, starting with normal,
    # then top right to bottom left
    diags = get_std_diagonals(matrix)
    diags += get_std_diagonals(np.rot90(matrix))
    return diags
