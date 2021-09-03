import numpy as np

positions = [[1, 2, 4], [6, 3, 8], [9, 2, 7]]
velocities = [[15, 7, 32], [7, 41, 32], [8, 4, 9]]
accelerations = [[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]]

nb_steps = 3
time_step = 0.001

pos_val = []
for (vel, acc) in zip(velocities, accelerations):
    pos = []
    for (v, a) in zip(vel, acc):
        pos.append(v * time_step + a * 0.5 * time_step ** 2)
    pos_val.append(pos)

positions1 = []
for (pos_val1, pos1) in zip(pos_val, positions):
    pos_1 = []
    for (pos_val0, pos0) in zip(pos_val1, pos1):
        pos_1.append(pos_val0 + pos0)
    positions1.append(pos_1)
positions = positions1

print(positions)

positions = np.array([[1, 2, 4], [6, 3, 8], [9, 2, 7]])
velocities = np.array([[15, 7, 32], [7, 41, 32], [8, 4, 9]])
accelerations = np.array([[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]])

positions = sum(np.multiply(velocities, time_step), 0.5 * np.multiply(accelerations, time_step ** 2)) + positions

print(positions)
