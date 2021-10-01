import numpy as np

k = np.array([[1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]]
    )
print(np.sum(k, axis = 0))
s = np.array([10, 20, 30])

_sum = np.add(np.sum(k, axis = 0), s)
print(_sum)

s1 = np.array([[10, 20, 30], [40, 50, 60]])

_sum1 = np.add(np.sum(k, axis = 0), s1[0: 3])
print(_sum1)

k_list = [[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]

s = [10, 20, 30]

#for index_p0 in range(15):
#    for index_p1 in range(index_p0 + 1, 16):
#        kk = [i for i in K_list]
#        _num[index_p0] 

#k1 = 0
#_num = [sum(i) for i in zip([j * 2 for j in i] for i in k_list], 
#print(_num)

#_sum1 = [sum(i) for i in zip(_num, s)]   
#print(_sum1)
