import numpy as np
import timeit

k = np.array([[0.065, 0.098, 0.043], [0.016, 0.842, 0.876]])

def square():
    s = np.square(k)

def power():
    s = np.power(k, 2)

def math():
    s = k ** 2

print('square', timeit.timeit('square()', globals = globals(), number = 100000))
print('power', timeit.timeit('power()', globals = globals(), number = 100000))
print('math', timeit.timeit('math()', globals = globals(), number = 100000))
