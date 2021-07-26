import sys
import math
import time

from datetime import timedelta

import numpy as np
import pandas as pd

from transonic import boost


def load_input_data(path):
    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter = r"\s+"
    )

    # warning: copy() is for Pythran...
    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()

    return masses, positions, velocities


def advance_positions(positions, velocities, accelerations, time_step):
    positions_ra = positions.ravel()
    velocities_ra = velocities.ravel()
    accelerations_ra = accelerations.ravel()
    positions_ra += time_step * velocities_ra + 0.5 * accelerations_ra * time_step ** 2

def advance_velocities(velocities, accelerations, accelerations1, time_step):
    velocities_ra = velocities.ravel()
    accelerations_ra = accelerations.ravel()
    accelerations1_ra = accelerations1.ravel()
    velocities_ra += 0.5 * time_step * (accelerations_ra + accelerations1_ra)



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


@boost
def transonic_boost(
    time_step: float,
    nb_steps: int,
    masses: "float[]",
    positions: "float[:,:]",
    velocities: "float[:,:]",
):

    accelerations = np.zeros_like(positions)
    accelerations1 = np.zeros_like(positions)

    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(nb_steps):
        advance_positions(positions, velocities, accelerations, time_step)
        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        compute_accelerations(accelerations, masses, positions)
        advance_velocities(velocities, accelerations, accelerations1, time_step)

        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            # f-strings supported by Pythran>=0.9.8
            #print(
            #    f"t = {time_step * step:5.2f}, E = {energy:.7f}, "
            #    f"dE/E = {(energy - energy_previous) / energy_previous:+.7f}"
            #)
            energy_previous = energy

    #return energy, energy0
    return math.floor((10000000*energy)/10000000), math.floor((10000000*energy)/10000000)

def compute_kinetic_energy(masses, velocities):
    return 0.5 * sum(masses * np.sum(velocities ** 2, 1))

def compute_potential_energy(masses, positions):
    nb_particules = masses.size
    pe = 0.0
    vector = np.empty(3)
    for index_p0 in range(nb_particules - 1):
        mass0 = masses[index_p0]
        position0 = positions[index_p0]
        for index_p1 in range(index_p0 + 1, nb_particules):

            for i in range(3):
                vector[i] = position0[i] - positions[index_p1, i]

            # vector = position0 - positions[index_p1]
            distance = math.sqrt(sum(vector ** 2))
            pe -= (mass0 * masses[index_p1]) / distance
    return pe


def compute_energies(masses, positions, velocities):
    energy_kin = compute_kinetic_energy(masses, velocities)
    energy_pot = compute_potential_energy(masses, positions)
    return energy_kin + energy_pot, energy_kin, energy_pot


if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    nb_steps = int(time_end / time_step) + 1

    path_input = "input16.txt"
    masses, positions, velocities = load_input_data(path_input)
    
    start = time.time()
    energy, energy0 = transonic_boost(time_step, nb_steps, masses, positions, velocities)
    end = time.time()

    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(
        f"{nb_steps} time steps run in {timedelta(seconds=start-end)}"
    )
