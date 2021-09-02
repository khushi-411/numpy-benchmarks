import sys
import math
import timeit
import cProfile

import numpy as np
import pandas as pd

from numba import njit
jit = njit(cache = True, fastmath = True)

def load_input_data(path):
    df = pd.read_csv(
        path, names = ["mass", "x", "y", "z", "vx", "vy", "vz"], delimiter=r"\s+"
    )
    masses = df["mass"].values.copy()
    positions = df.loc[:, ["x", "y", "z"]].values.copy()
    velocities = df.loc[:, ["vx", "vy", "vz"]].values.copy()
    
    return masses, positions, velocities

@jit
def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size

    for index_p0 in range(nb_particles - 1):
        
        position0 = positions[index_p0]
        mass0 = masses[index_p0]

        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]

            vector = position0 - positions[index_p1]
        
            distance = np.square(vector).sum()
            coef = distance ** 1.5
    
            accelerations[index_p0] = mass1 * -1 * vector / coef + accelerations[index_p0]
            accelerations[index_p1] = mass0 * vector / coef + accelerations[index_p1]
    
    return accelerations

@jit
def numba_loop(
        time_step: float, 
        number_of_steps: int, 
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
    
    for step in range(number_of_steps):

        positions = sum(np.multiply(velocities, time_step), 0.5 *  np.multiply(accelerations, time_step ** 2)) + positions
    
        accelerations, accelerations1 = accelerations1, accelerations
        accelerations.fill(0)
        
        accelerations = compute_accelerations(accelerations, masses, positions)
        
        velocities = 0.5 * np.multiply(time_step, np.add(accelerations, accelerations1)) + velocities

        time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            energy_previous = energy

    return energy, energy0

@jit
def compute_energies(masses, positions, velocities): 

    ke = 0.5 * (np.multiply(masses, np.square(velocities).sum(axis = 1)).sum())
    number_of_particles = masses.size
    pe = 0.0
    for index_p0 in range(number_of_particles - 1):

        mass = masses[index_p0]
        for index_p1 in range(index_p0 + 1, number_of_particles):
            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]
            distance = np.sqrt((vector ** 2).sum())
        
            pe = np.subtract(np.divide(np.multiply(mass, mass1), distance), pe)

    return ke + pe, ke, pe

def main(time_step, nb_steps, masses, positions, velocities):
    #cProfile('numba_loop(time_step, nb_steps, masses, positions, velocities')
    print('time taken:', timeit.timeit("numba_loop(time_step, nb_steps, masses, positions, velocities)", globals = globals(), number = 1))

if __name__ == "__main__":

    try:
        time_end = float(sys.argv[2])
    except IndexError:
        time_end = 10.0

    time_step = 0.001
    nb_steps = int(time_end/time_step) + 1

    path_input = sys.argv[1]
    masses, positions, velocities = load_input_data(path_input)
    main(time_step, nb_steps, masses, positions, velocities)