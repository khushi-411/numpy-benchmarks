import sys
import math
import time
import timeit
import cProfile
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

"""
# distance travelled = sqrt( (x_i - x_j) ** 2 + (y_i - y_j) ** 2 + (z_i - z_j) ** 2 )
def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size
    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]
        mass1 = masses[index_p0+1:nb_particles]
        position1 = positions[index_p0+1:nb_particles]
        # vector = (x_i - x_j) // 1-d, 3-axis 
        vector = position0 - position1
        # dis = power(dis, 3/2)
        distance = np.square(vector).sum() * np.sqrt(np.square(vector).sum())  # check this

        coef_m1 = mass0 / distance
        coef_m2 = mass1 / distance
        accelerations[index_p0] -= np.sum(coef_m1 * vector)
        #print(accelerations[index_p0])
        accelerations[index_p0+1:nb_particles] += np.sum(coef_m2 * vector)            
        
    return accelerations

"""

"""Computing accelerations of two body"""
def compute_accelerations(accelerations, masses, positions):
    nb_particles = masses.size
    for index_p0 in range(nb_particles - 1):
        position0 = positions[index_p0]
        mass0 = masses[index_p0]
        for index_p1 in range(index_p0 + 1, nb_particles):
            mass1 = masses[index_p1]
            # vector = [0.453, 0.874, 0.086]
            vector = position0 - positions[index_p1]
            #dist = np.linalg.norm(vector)
            # dis = 0.0432
            distance = np.square(vector).sum()
            #coef = np.sqrt(distance) * distance
            coef = distance ** 1.5
            # a1 = G * m2 * (r2 - r1) / dist ** 3/2
            # a2 = G * m1 * (r1 - r2) / dist ** 3/2
            # accelerations[index_p0] = [0.042, 0.0234, 0.0532]
            accelerations[index_p0] -= mass1 * vector / coef
            accelerations[index_p1] += mass0 * vector / coef
    #print('index_p0', accelerations[index_p0])
    #print('index_p1', accelerations[index_p1])
    #print(accelerations)
    # acc = [[], [], [], [], []]
    return accelerations

def optimized_numpy(
        time_step: float, 
        number_of_steps: int, 
        masses: "float[]", 
        positions: "float[:,:]", 
        velocities: "float[:,:]",
    ):
    
    """Creating variable for acceleration and initializing with zero"""
    
    accelerations = np.zeros(positions.shape, dtype = float)
    accelerations1 = np.zeros(positions.shape, dtype = float)

    """Calculaing initial accelerations of particle, due to their self potential energyand kinetic energy"""
    accelerations = compute_accelerations(accelerations, masses, positions)
    #t = timeit.Timer('compute_accelerations(accelerations, masses, positions)')
    #t.timeit()
    _time = 0.0
   
    energy0, _, _ = compute_energies(masses, positions, velocities)
    energy_previous = energy0
    
    for step in range(number_of_steps):
        positions += sum(np.multiply(velocities, time_step), 0.5 *  np.multiply(accelerations, time_step ** 2))
        #print('before accelerations', accelerations)
        #print('before accelerations1', accelerations1)
        accelerations, accelerations1 = accelerations1, accelerations
        #print('accelerations', accelerations)
        #print('accelerations1', accelerations1)
        accelerations.fill(0)
        #print(accelerations)
        accelerations = compute_accelerations(accelerations, masses, positions)
        #cProfile.run('compute_accelerations(accelerations, masses, positions)')
        velocities += 0.5 * np.multiply(time_step, np.add(accelerations, accelerations1))

        _time += time_step

        if not step % 100:
            energy, _, _ = compute_energies(masses, positions, velocities)
            #print(
            #    f"t = {time_step * step:5.2f}, E = {energy:.7f}, "
            #    f"dE/E = {(energy - energy_previous) / energy_previous:+.7f}"
            #)
            energy_previous = energy
    return energy, energy0

#def pt_en(mass, mass1, distance, pe):
#    return  np.subtract(np.divide(np.multiply(mass, mass1), distance), pe)

def compute_energies(masses, positions, velocities): 
    # ke = 0.883623
    ke = 0.5 * (np.multiply(masses, np.square(velocities).sum(axis = 1)).sum())
    number_of_particles = masses.size
    pe = 0.0
    for index_p0 in range(number_of_particles - 1):

        mass = masses[index_p0]
        for index_p1 in range(index_p0 + 1, number_of_particles):
            mass1 = masses[index_p1]
            vector = positions[index_p0] - positions[index_p1]
            distance = np.sqrt((vector ** 2).sum())
            # pe = 0.976
            pe = np.subtract(np.divide(np.multiply(mass, mass1), distance), pe)
            #pe = pt_en(mass, mass1, distance, pe)
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
    cProfile.run('optimized_numpy(time_step, number_of_steps, masses, positions, velocities)')
   #for i in range(5):
   # energy, energy0 =
    #print('time taken: ', timeit.timeit("optimized_numpy(time_step, number_of_steps, masses, positions, velocities)", globals = globals(), number = 5))

    #print(f"Final dE/E = {(energy - energy0) / energy0:.7e}")
   # print(
   #         f"{number_of_steps} time steps run in {timedelta(seconds=end-start)}"
   # )
