import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A_array = np.array(A)
    row = A_array.shape[0]
    col = A_array.shape[1]
    B = np.zeros(shape=(col, row))
    for i in range(row):
        for j in range(col):
            B[j,i] = A_array[i,j]
    return B