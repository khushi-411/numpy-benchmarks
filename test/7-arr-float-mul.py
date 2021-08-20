import numpy as np
import timeit

k = np.array([0.065, 0.065, 0.065])
s = np.array([0.023, 0.043, 0.053])

def multiply():
    a = np.multiply(k, s)
    print(a)

def dot():
    a = np.dot(k, s)

def math():
    a = k * s
    print(a)

print('multiply', timeit.timeit('multiply()', globals = globals(), number = 100))
print('dot', timeit.timeit('dot()', globals = globals(), number = 1))
print('math', timeit.timeit('math()', globals = globals(), number = 100))
