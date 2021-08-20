import numpy as np
import timeit

k = np.float64(0.08)
#print(type(k))

s = np.float64(0.97)

def multiply():
    a = np.multiply(k, s)

def dot():
    a = np.dot(k, s)

def math():
    a = k * s

print('multiply', timeit.timeit('multiply()', globals = globals(), number = 100000))
print('dot', timeit.timeit('dot()', globals = globals(), number = 100000))
print('math', timeit.timeit('math()', globals = globals(), number = 100000))
