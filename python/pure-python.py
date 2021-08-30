import sys
import math
import cProfile

import numpy as np
import pandas as pd

def load_input_data(path):
    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter = r"\s+"
    )

    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()

    return masses, positions, velocities


def compute_accelerations(accelerations, masses, positions):
    nb_particles = len(masses)
    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]
        
        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]

            vector = [p0 - p1 for (p0, p1) in zip(position0, positions[index_p1])]

            distance = 0
            for i in vector:
                distance += i ** 2         # pow(i, 2)
            
            coefs = distance ** 1.5
                
            if accelerations[index_p0] == float(0) and accelerations[index_p1] == float(0):
                accelerations[index_p0] = [sum(i) for i in zip([vec_val * mass1 * -1 / coefs for vec_val in vector], [accelerations[index_p0]])]
                accelerations[index_p1] = [sum(i) for i in zip([vec_val * mass0 / coefs for vec_val in vector], [accelerations[index_p1]])]
            
            elif accelerations[index_p0] == float(0) and accelerations[index_p1] != float(0):
                accelerations[index_p0] = [sum(i) for i in zip([vec_val * mass1 * -1 / coefs for vec_val in vector], [accelerations[index_p0]])]
                accelerations[index_p1] = [sum(i) for i in zip([vec_val * mass0 / coefs for vec_val in vector], accelerations[index_p1])]

            elif accelerations[index_p0] != float(0) and accelerations[index_p1] == float(0.0):
                accelerations[index_p0] = [sum(i) for i in zip([vec_val * mass1 * -1 / coefs for vec_val in vector], accelerations[index_p0])]
                accelerations[index_p1] = [sum(i) for i in zip([vec_val * mass0 / coefs for vec_val in vector], [accelerations[index_p1]])]

            else:
                accelerations[index_p0] = [sum(i) for i in zip([vec_val * mass1 * -1 / coefs for vec_val in vector], accelerations[index_p0])]
                accelerations[index_p1] = [sum(i) for i in zip([vec_val * mass0 / coefs for vec_val in vector], accelerations[index_p1])]

    return accelerations


def loop(
    time_step: float,
    nb_steps: int,
    masses: "float[]",
    positions: "float[:,:]",
    velocities: "float[:,:]",
):

    accelerations = [float(0) for i in range(len(positions))]
    accelerations1 = [float(0) for i in range(len(positions))]
    
    accelerations = compute_accelerations(accelerations, masses, positions)
    
    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(nb_steps):
        pos_val = []
        for (vel, acc) in zip(velocities, accelerations):
            print('vel', vel)
            print('acc', acc)
            pos = []
            for (v, a) in zip(vel, acc):
                pos.append(sum(v * time_step, a * 0.5 * time_step ** 2))
            pos_val.append(pos)
        print(pos_val)
        #pos = [[ut[i][j] + at[i][j] for j in range(len(ut[0]))] for i in range(len(ut))]
        #print(pos)
        #pos = list(map(sum, zip(*i)) for i in zip(ut, at))
        #print(pos)
        print()
        positions = [map(sum, zip(*i)) for i in zip(pos, positions)] #[sum(i) for i in zip(pos, positions)]
        print(positions)
        accelerations, accelerations1 = accelerations1, accelerations
        #print(accelerations)
        #accelerations.fill(0)
        accelerations = compute_accelerations(accelerations, masses, positions)
        velocities = 0.5 * time_step * (accelerations + accelerations1) + velocities
        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            energy_previous = energy

    return energy, energy0


def compute_energies(masses, positions, velocities):

    vel = []
    for ind, val in enumerate(velocities):
        vel.append([j ** 2 for j in val])
    val = []
    for i in vel:
        k = 0
        for j in i:
            k += j
        val.append(k)
    ke_list = [0.5 * i * masses[ind] for ind, i in enumerate(val)]
    ke = 0.0
    for i in ke_list:
        ke += i

    nb_particules = len(masses)
    pe = 0.0
    for index_p0 in range(nb_particules - 1):
        mass0 = masses[index_p0]
        for index_p1 in range(index_p0 + 1, nb_particules):
            mass1 = masses[index_p1]
            vector = [p0 - p1 for (p0, p1) in zip(positions[index_p0], positions[index_p1])]
            dist = 0
            for i in vector:
                dist += i ** 2
            distance = math.sqrt(dist)
            pe -= (mass0 * mass1) / distance

    return ke + pe, ke, pe


if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.

    time_step = 0.001
    nb_steps = int(time_end / time_step) + 1

    path_input = sys.argv[1]
    masses, positions, velocities = load_input_data(path_input)
    masses = masses.tolist()
    positions = positions.tolist()
    velocities = velocities.tolist()

    cProfile.run('loop(time_step, nb_steps, masses, positions, velocities)')
