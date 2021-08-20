import numpy as np
import timeit

k = np.array([[0.065, 0.065, 0.065], [0.065, 0.065, 0.065]])

# print(type(k))
# print((type(k[1][1])))

def zeros_like():
    s = np.zeros_like(k)

def zeros():
    s = np.zeros(k.shape, dtype=float)

print('zeros_like', timeit.timeit('zeros_like()', globals=globals(), number=100))

print('zeros', timeit.timeit('zeros()', globals=globals(), number=100))
