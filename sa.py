import numpy as np
import matplotlib.pyplot as plt
import time
import argparse
from common import load_matrices

def parse_arguments():
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('--N', type=int, default=5, help="Parameter type (default: 5)")
    parser.add_argument('--Mcycle', type=int, default=40000, help="Mcycle (default: 40000)")
    parser.add_argument('--trial', type=int, default=100, help="trial (default: 100)")
    parser.add_argument('--T_ini', type=float, default=1000, help="T_ini (default: 1000)")
    parser.add_argument('--T_end', type=float, default=0.1, help="T_end (default: 1)")
    parser.add_argument('--tau', type=int, default=1, help="tau (default: 1)")
    return parser.parse_args()

def simulated_annealing(J, h, T_ini, T_end, Mcycle, tau, len_H1, true_min_energy):
    Cr = pow(T_end / T_ini, 1 / Mcycle)
    energy = np.zeros(Mcycle + 1)
    T = np.zeros(Mcycle + 1)
    
    # Initialize
    mi = 2 * np.random.randint(2, size=(len_H1, 1)) - 1
    mo = np.zeros((len_H1, Mcycle + 1))
    mo[:, 0] = mi[:, 0]

    Jm_temp = J @ mi
    hm_temp = np.transpose(h) @ mi
    energy[0] = -np.sum(Jm_temp * mi) / 2 - hm_temp
    
    # Start time
    start_time = time.time()

    # Annealing process
    for t in range(1, Mcycle + 1):
        if t == 1:
            T[t] = T_ini
        elif t % tau == 0:
            T[t] = T[t - 1] * Cr if T_end < T[t - 1] else T_ini
        else:
            T[t] = T[t - 1]

        select = np.random.randint(len_H1)
        mo[:, t] = mi[:, 0]
        mo[select, t] = -mo[select, t]

        Jm_temp = J @ mo[:, t]
        hm_temp = np.transpose(h) @ mo[:, t]
        energy[t] = -np.sum(Jm_temp * mo[:, t]) / 2 - hm_temp

        deltaE = energy[t] - energy[t - 1]
        P = np.exp(-deltaE / T[t])

        if P > np.random.rand():
            mi[select, 0] = -mi[select, 0]
        else:
            energy[t] = energy[t - 1]
            mo[select, t] = mi[select, 0]

    # End time
    elapsed_time = time.time() - start_time

    # Check if solution is correct
    is_correct = 0
    if np.min(energy) == true_min_energy:
        is_correct = 1
        print(f'try{run} OK, energy =', np.min(energy), ', time = ', elapsed_time)
    else:
        print(f'try{run} NG, energy =', np.min(energy), ', time = ', elapsed_time)

    return energy, T, elapsed_time, is_correct

def plot_results(energy, T, Mcycle):
    plt.figure(figsize=(10, 5))

    # Plot energy
    plt.subplot(2, 1, 1)
    plt.plot(energy)
    plt.ylabel('Energy')
    plt.xlabel('Cycle')
    plt.grid(True)

    # Plot temperature
    plt.subplot(2, 1, 2)
    plt.plot(T)
    plt.ylabel('Temperature T')
    plt.xlabel('Cycle')
    plt.xlim([0, Mcycle])
    plt.grid(True)

    # Show plots
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    args = parse_arguments()

    N = args.N
    run_c = args.trial
    T_ini = args.T_ini
    T_end = args.T_end
    Mcycle = args.Mcycle
    tau = args.tau
    Cr = pow(T_end / T_ini, 1 / Mcycle)

    J, h = load_matrices(N)

    # Calculate minimum energy
    m = np.ones((N * N, 1)) * -1
    for i in range(N):
        for j in range(N):
            if i == j:
                m[i * N + j, 0] = 1
    Jm_temp_min = J @ m
    hm_temp_min = np.transpose(h) @ m
    true_min_energy = -np.sum(Jm_temp_min * m) / 2 - hm_temp_min
    print('min_energy=',true_min_energy)

    times = np.zeros(run_c)
    correct = 0

    for run in range(run_c):
        energy, T, elapsed_time, is_correct = simulated_annealing(J, h, T_ini, T_end, Mcycle, tau, N * N, true_min_energy)
        times[run] = elapsed_time
        correct += is_correct
        
    print('Mean time =', np.sum(times) / run_c)
    print('Acc [%]=', correct / run_c)

    plot_results(energy, T, Mcycle)
