import numpy as np

def load_matrices(N):
    # Construct the filenames based on N
    j_filename = f'./graph/J_N{N}.txt'
    h_filename = f'./graph/h_N{N}.txt'

    # Load the matrices from text files into NumPy arrays
    J = np.loadtxt(j_filename)
    h = np.loadtxt(h_filename)

    return J, h
