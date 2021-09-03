import numpy as np

positions = [[1, 2, 4], [6, 3, 8], [9, 2, 7]]
velocities = [[15, 7, 32], [7, 41, 32], [8, 4, 9]]
accelerations = [[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]]
accelerations1 = [[0.0 for _ in range(3)] for _ in range(3)]
masses = [5, 5, 5]

nb_steps = 3
time_step = 0.001

velocities1 = []
for (acc, vel) in zip(accelerations1, velocities):
    vel1 = []
    for (a, v) in zip(acc, vel):
        vel1.append(time_step * a + v)
    velocities1.append(vel1)
velocities = velocities1
print(type(velocities[0][0]))
print(velocities)
print()

positions = np.array([[1, 2, 4], [6, 3, 8], [9, 2, 7]])
velocities = np.array([[15, 7, 32], [7, 41, 32], [8, 4, 9]])
accelerations = np.array([[0.10420362287369969, 0.1635408522010455, -0.002114445027585069], [0.06472460636268612, -0.26259450716105587, 0.30683522207209835], [-0.1689282292363858, 0.09905365496001035, -0.3047207770445133]])
accelerations1 = np.zeros_like(accelerations)
masses = np.array([5, 5, 5])

velocities = 0.5 * np.multiply(time_step, np.add(accelerations, accelerations1)) + velocities
print(type(velocities[0][0]))
print(velocities)
