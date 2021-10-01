import numpy as np
import timeit

k = np.array([[0.098, 0.092, 0.062], [0.087, 0.087, 0.055]])

def sum():
    s = np.sum(k, axis = 1)

def ndarray_sum():
    s = k.sum(axis = 1)

print('sum', timeit.timeit('sum()', globals = globals(), number = 1))
print('ndarray_sum', timeit.timeit('ndarray_sum()', globals = globals(), number = 1))
