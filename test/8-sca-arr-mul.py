import numpy as np
import timeit

k = np.array([0.0923, 0.0865, 0.0987])
s = 0.5

def multiply():
    a = np.multiply(s, k)

def dot():
    a = np.dot(s, k)

def math():
    a = s * k

print('multiply', timeit.timeit('multiply()', globals = globals(), number = 100000))
print('dot', timeit.timeit('dot()', globals = globals(), number = 100000))
print('math', timeit.timeit('math()', globals = globals(), number = 100000))
