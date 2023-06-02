import numpy as np

def create_matrix():
    matrix = np.diag(np.arange(50))
    return matrix

def save_matrix():
    matrix = create_matrix()
    np.save('exercici1.npy', matrix)