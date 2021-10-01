import numpy as np

positions = [[1, 2, 4], [6, 3, 8], [9, 2, 7]]
velocities = [[15, 7, 32], [7, 41, 32], [8, 4, 9]]
accelerations = [[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]]
masses = [5, 5, 5]

nb_steps = 3
time_step = 0.001

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

print(ke)

positions = np.array([[1, 2, 4], [6, 3, 8], [9, 2, 7]])
velocities = np.array([[15, 7, 32], [7, 41, 32], [8, 4, 9]])
accelerations = np.array([[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]])
masses = np.array([5, 5, 5])

ke = 0.5 * (np.multiply(masses, np.square(velocities).sum(axis = 1)).sum())
print(ke)
