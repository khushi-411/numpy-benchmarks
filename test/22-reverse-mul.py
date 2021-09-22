import numpy as np
import timeit

k1 = np.array([[0.0923, 0.0865, 0.0987], [0.532, 0.1244, 0.2355]])
k2 = np.array([[0.353, 0.456, 0.426], [0.134, 0.645, 0.264]])
s = 0.001

def mul():
    velo = 0.5 * np.multiply(s, np.add(k1, k2))

def math():
    velo = 0.5 * 0.001 * np.add(k1, k2)

print('math', timeit.timeit('math()', globals = globals(), number = 1000000))
print('multiply', timeit.timeit('mul()', globals = globals(), number = 1000000))
