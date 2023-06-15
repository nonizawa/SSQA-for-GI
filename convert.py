import numpy as np
from scipy.io import loadmat
import argparse


def load_dataset():
    return loadmat('GI_p50_dataset.mat')

def parse_arguments():
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('--N', type=int, default=5, help="Parameter type (default: 5)")
    return parser.parse_args()

def select_g1e(dataset, N):
    key = f'G{N}'
    if key in dataset:
        return dataset[key]
    else:
        raise ValueError(f"Dataset does not contain data for N={N}")

def generate_hamiltonian(N, G1E, G2E, C1=1, C2=1):
    H1 = np.zeros((N * N, N * N))
    # Add C1 penalty to the Hamiltonian
    for u in range(N):
        for i in range(N):
            for v in range(u, N):
                for j in range(N):
                    if i == j and u == v:
                        H1[u * N + i, v * N + j] = -C1
                    elif i == j or u == v:
                        H1[u * N + i, v * N + j] = H1[u * N + i, v * N + j] + C1

    # Add C2 penalty to the Hamiltonian
    for u in range(N):
        for v in range(u, N):
            if u != v:
                for i in range(N):
                    for j in range(N):
                        if i != j:
                            if G2E[u, v] != G1E[i, j]:
                                H1[u * N + i, v * N + j] = H1[u * N + i, v * N + j] + C2

    len_H1 = len(H1)
    H = np.copy(H1)

    # Convert from QUBO format to Ising model for Hamiltonian
    J = H / 4

    for i in range(len_H1):
        for j in range(len_H1):
            if i > j:
                J[i, j] = J[j, i]
            elif i == j:
                J[i, j] = 0

    h = np.zeros((len_H1, 1))
    for i in range(len_H1):
        h[i, 0] = H[i, i] / 2 + np.sum(J[i, :])

    h = -h
    J = -J

    return J, h

if __name__ == "__main__":
    dataset = load_dataset()
    args = parse_arguments()

    N = args.N

    G1E = select_g1e(dataset, N)
    G2E = np.copy(G1E)
  
    J, h = generate_hamiltonian(N, G1E, G2E)

    # Save J and h matrices to text files with N in the filename
    np.savetxt(f'./graph/J_N{N}.txt', J, fmt='%f')
    np.savetxt(f'./graph/h_N{N}.txt', h, fmt='%f')
