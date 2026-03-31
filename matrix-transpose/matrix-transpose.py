import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    An = np.array(A)
    i,j = An.shape
    AT = np.zeros((j, i), dtype=An.dtype)
    for row in range(i):
        for col in range(j):
            AT[col, row] = An[row, col]
    pass
    return AT
