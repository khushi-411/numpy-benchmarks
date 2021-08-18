import sys
import math
import time
from datetime import timedelta

import numpy as np
import pandas as pd

def load_input_data(path):
    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter=r"\s+"
    )
    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()
    return masses, positions, velocities


def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size
    for index_p0 in range(nb_particles - 1):

        position0 = positions[index_p0]
        mass0 = masses[index_p0]

        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]
            position1 = positions[index_p1]
            
            vector = position0 - position1
            distance = np.add(np.square(vector)) * np.sqrt(np.add(np.square(vector)))
        
            coef_m1 = np.divide(mass0, distance) 
            coef_m2 = np.divide(mass1, distance)
               
            accelerations[index_p0] -= np.multiply(coef_m1, vector)
            accelerations[index_p1] += np.multiply(coef_m2, vector)
    return accelerations


def optimized_numpy(
        time_step: float, 
        number_of_steps: int, 
        masses: "float[]", 
        positions: "float[:,:]", 
        velocities: "float[:,:]",
    ):
    
    accelerations = np.zeros_like(positions)
    accelerations1 = np.zeros_like(positions)

    # Initial Acceleration
    accelerations = compute_accelerations(accelerations, masses, positions)

    time = 0.0
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0

    for step in range(number_of_steps):
        
        positions += sum(np.dot(velocities, time_step), np.dot(0.5, np.dot(accelerations, np.square(time_step))))
        
        # Swapping accelerations 
        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        accelerations = compute_accelerations(accelerations, masses, positions)
        
        # Use sum() or np.add()? (time sum() < time np.add())
        velocities += np.dot(0.5, np.dot(time_step, sum(accelerations, accelerations1)))
        
        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            #print(
            #    f"t = {time_step * step:5.2f}, E = {energy:.7f}, "
            #    f"dE/E = {(energy - energy_previous) / energy_previous:+.7f}"
            #)
            energy_previous = energy
    return energy, energy0


def compute_energies(masses, positions, velocities):
    
    ke = np.multiply(0.5, np.sum(np.multiply(masses,np.add(np.square(velocities), 1))))

    number_of_particles = masses.size
    pe = 0.0
    for index_p0 in range(number_of_particles - 1):
        mass = masses[index_p0]
        for index_p1 in range(index_p0 + 1, number_of_particles):
            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]
            distance = np.sqrt(sum(np.square(vector)))
            pe = np.subtract(np.divide(np.multiply(mass, mass1), distance), pe)

    return ke + pe, ke, pe

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    number_of_steps = int(time_end/time_step) + 1

    path_input = sys.argv[1]
    
    masses, positions, velocities = load_input_data(path_input)
    
    start = time.time()
    for i in range(5):
        energy, energy0 = optimized_numpy(time_step, number_of_steps, masses, positions, velocities)
    end = time.time()

    print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
    print(
            f"{number_of_steps} time steps run in {timedelta(seconds=end-start)}"
    )

