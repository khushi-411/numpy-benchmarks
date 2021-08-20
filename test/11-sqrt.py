import numpy as np
import timeit
import math

k = np.array([0.0223, 0.0334, 0.0864])

def numpy_sqrt():
    s = np.sqrt(k)
    print(s)

def math_sqrt():
    s = math.sqrt(k)
    print(s)

print('numpy_sqrt', timeit.timeit('numpy_sqrt()', globals = globals(), number = 1))
print('math_sqrt', timeit.timeit('math_sqrt()', globals = globals(), number = 1))
