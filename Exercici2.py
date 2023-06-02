import numpy as np

def matrix1():
    matrix = np.zeros((4, 4))
    matrix[2, :] = 2
    matrix[:, 3] = 3
    return matrix

def matrix2():
    matrix = np.ones((5, 5))
    matrix[1:4, 1:4] = 0
    return matrix

def matrix3():
    matrix = np.eye(3)
    matrix += 3
    return matrix