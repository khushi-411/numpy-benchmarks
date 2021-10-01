import numpy as np
import timeit

k = np.array([[0.065, 0.365, 0.893], [0.464, 0.514, 0.515]])
a = 0.001

print(type(k))
print(type(k[1][1]))
print(type(a))

def dot():
    s = np.dot(k, a ** 2)

def multiply():
    s = np.multiply(k, a ** 2)

def math():
    s = k * (a ** 2)

print('dot', timeit.timeit('dot()', globals=globals(), number=100000))
print('multiply', timeit.timeit('multiply()', globals=globals(), number=100000))
print('math', timeit.timeit('math()', globals=globals(), number=100000))

