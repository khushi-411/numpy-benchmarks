import numpy as np
import timeit

k = np.array([0.0562, 0.0233, 0.0321])

def sub():
    s = np.subtract(k[1], k[0])

def math():
    s = k[1] - k[0]

print('sub', timeit.timeit('sub()', globals = globals(), number = 100000))
print('math', timeit.timeit('math()', globals = globals(), number = 100000))
