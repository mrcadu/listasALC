# Python3 program to decompose
# a matrix using Cholesky
# Decomposition
import math
from matrix import *

def decompose(matrix, n):
    lower = [[0 for _ in range(n)]
             for _ in range(n)]

    # Decomposing a matrix
    # into Lower Triangular
    for i in range(n):
        for j in range(i + 1):
            sum1 = 0
            # sum1mation for diagonals
            if j == i:
                for k in range(j):
                    sum1 += pow(lower[j][k], 2)
                lower[j][j] = int(math.sqrt(matrix[j][j] - sum1))
            else:
                # Evaluating L(i, j)
                # using L(j, j)
                for k in range(j):
                    sum1 += (lower[i][k] * lower[j][k])
                if lower[j][j] > 0:
                    lower[i][j] = int((matrix[i][j] - sum1) /
                                      lower[j][j])
    return lower, transpose(lower)
