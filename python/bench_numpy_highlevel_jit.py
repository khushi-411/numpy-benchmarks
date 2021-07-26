# Pythran Naive

import numpy as np
import pandas as pd

import math
from datetime import timedelta
import sys

from transonic import jit

import time

def load_input_data(path):
    df = pd.read_csv(
            path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter = r"\s+"
        )
    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()
    return masses, positions, velocities

def advance_positions(positions, velocities, accelerations, time_step):
    positions += velocities * time_step + 0.5 * accelerations * time_step ** 2

def advance_velocities(velocities, accelerations, accelerations1, time_step):
    velocities += 0.5 * time_step * (accelerations + accelerations1)

def compute_accelerations(accelerations, masses, positions):
    number_of_particles = masses.size
    for particle_1_index in range(number_of_particles - 1):
        position_1 = positions[particle_1_index]
        masses_1 = masses[particle_1_index]
        vector = np.empty(3)
        for particle_2_index in range(particle_1_index +1, number_of_particles):
            masses_2 = masses[particle_2_index]
            position_2 = positions[particle_2_index]
            for i in range(3):
                vector[i] = position_1[i] - position_2[i]
            
            distance = sum(vector ** 2) * math.sqrt(sum(vector ** 2))
            coef_m1 = masses_1 / distance
            coef_m2 = masses_2 / distance
            for i in range(3):
                accelerations[particle_1_index][i] -= coef_m1 * vector[i]
                accelerations[particle_2_index][i] += coef_m2 * vector[i]
    return accelerations


@jit
def pythran_naive(time_step, number_of_steps, masses, positions, velocities):
    accelerations_1 = np.zeros_like(positions)
    accelerations_2 = np.zeros_like(positions)

    # Initial Acceleration
    accelerations = compute_accelerations(accelerations_1, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(number_of_steps):
        advance_positions(positions, velocities, accelerations_1, time_step)
        accelerations_1, accelerations_2 = accelerations_2, accelerations_1
        accelerations_1.fill(0)
        compute_accelerations(accelerations_1, masses, positions)
        advance_velocities(velocities, accelerations_1, accelerations_2, time_step)
        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            #print(
            #    f"t = {time_step * step:5.2f}, E = {energy:.7f}, "
            #    f"dE/E = {(energy - energy_previous) / energy_previous:+.7f}"
            #)
            energy_previous = energy

    return math.floor((10000000*energy)/10000000), math.floor((10000000*energy0)/10000000)


def compute_kinetic_energy(masses, velocities):
    return 0.5 * np.sum(masses * np.sum(velocities ** 2, 1))

def compute_potential_energy(masses, positions):
    number_of_particles = masses.size
    pe = 0.0              
    for particle_1_index in range(number_of_particles -1):
        mass_1 = masses[particle_1_index]
        for particle_2_index in range(particle_1_index +1, number_of_particles):
            mass_2 = masses[particle_2_index]
            vector = positions[particle_1_index] - positions[particle_2_index]
            distance = math.sqrt(sum(vector**2))
            pe -= (mass_1 * mass_2) / distance
    return pe

def compute_energies(masses, positions, velocities):
    ke = compute_kinetic_energy(masses, velocities)
    pe = compute_potential_energy(masses, positions)
    return ke+pe, ke, pe

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    number_of_steps = int(time_end/time_step) +1

    path_input = "input16.txt"
    masses, positions, velocities = load_input_data(path_input)
    
    start = time.time()
    energy, energy0 = pythran_naive(time_step, number_of_steps, masses, positions, velocities)
    end = time.time()
    
    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(
            f"{number_of_steps} time steps run in {timedelta(seconds=end-start)}"
    )


