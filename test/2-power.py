import numpy as np
import timeit

k = np.float64(0.1)
print(type(k))

def power():
    s = np.power(k, 2)

def square():
    s = np.square(k)

def math():
    s = k ** 2

print('power', timeit.timeit('power()', globals = globals(), number=100000))
print('square', timeit.timeit('square()', globals = globals(), number=100000))
print('math', timeit.timeit('math()', globals = globals(), number=100000))
