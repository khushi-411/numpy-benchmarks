import numpy as np
import timeit

k = np.array([[0.023, 0.043, 0.024], [0.053, 0.035, 0.065]])
s = np.array([[0.045, 0.056, 0.073], [0.034, 0.075, 0.089]])

print(type(k))
print(type(k[1][2]))

def sum():
    result = k + s

def add():
    result = np.add(k, s)

def array_add():
    result = k + s

print('sum', timeit.timeit('sum()', globals = globals(), number = 100000))
print('add', timeit.timeit('add()', globals = globals(), number = 100000))
print('array_add', timeit.timeit('array_add()', globals=globals(), number = 100000))
