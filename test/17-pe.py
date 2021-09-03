import numpy as np
import math

positions = [[1, 2, 4], [6, 3, 8], [9, 2, 7]]
velocities = [[15, 7, 32], [7, 41, 32], [8, 4, 9]]
accelerations = [[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]]

masses = [5, 5, 5]

nb_particules = len(masses)
time_step = 0.001

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
        pe = (mass0 * mass1) / pow(distance, 2) - pe

print(pe)
print()

positions = np.array([[1, 2, 4], [6, 3, 8], [9, 2, 7]])
velocities = np.array([[15, 7, 32], [7, 41, 32], [8, 4, 9]])
accelerations = np.array([[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]])

masses = np.array([5, 5, 5])
pe = 0.0
for index_p0 in range(nb_particules - 1):

    mass0 = masses[index_p0]
    for index_p1 in range(index_p0 + 1, nb_particules):
        mass1 = masses[index_p1]
        vector = positions[index_p0] - positions[index_p1]
        distance = np.sqrt((vector ** 2).sum())
        pe = np.subtract(np.divide(np.multiply(mass0, mass1), np.square(distance)), pe)

print(pe)
