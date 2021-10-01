import numpy as np

#k1 = [[100, 20, 30], [40, 123, 15], [11, 8, 15]]
k1 = [[1, 2, 3], [4, 9, 1], [5, 7, 4]]
s1 = [5, 5, 5]
acc1 = [[0.0 for acc0 in acc1] for acc1 in k1]

n1 = len(s1)

for i in range(n1 - 1):
    k0 = k1[i]
    s0 = s1[i]
    for j in range(i + 1, n1):
        s_1 = s1[j]
        vec = [p0 - p1 for (p0, p1) in zip(k0, k1[j])]
        dist = 0
        for ii in vec:
            dist += pow(ii, 2)
        coefs = dist ** 1.5
        acc1[i] = [sum(l) for l in zip([vec_val * s_1 * -1 / coefs for vec_val in vec], acc1[i])]
        acc1[j] = [sum(l) for l in zip([vec_val * s0 / coefs for vec_val in vec], acc1[j])]
        
print('list acc1', acc1)
print()

k2 = np.array([[1, 2, 3], [4, 9, 1], [5, 7, 4]])
s2 = np.array([5, 5, 5])
acc2 = np.zeros_like(k1)

n2 = s2.size

for i in range(n1 - 1):
    k0 = k2[i]
    s0 = s2[i]
    vec = k0 - k2[i + 1 : n2]
    dist = np.square(vec).sum(axis = 1)
    coefs = dist ** 1.5
    acc2[i] = np.sum(
            np.divide(
                np.multiply(s2[i + 1 : n2], -1 * vec.T), coefs
            )
        )
    acc2[i + 1 : n2] = np.sum(
            np.divide(
                s0 * vec.T, coefs
            )
        )
print('numpy array acc1', acc1)
