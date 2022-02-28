#!/usr/bin/env python3

import numpy as np

#the letter of the array corresponds with the exercise

a = np.zeros(10)
a[4] = 1
print(a)

b = np.arange(10,50)
print(b)

c = b[::-1] #reversing a vector
print(c)

d = np.reshape(np.arange(0,9), (3,3))
print(d)

e = np.argwhere(np.array([1,2,0,0,4,0])) #finds indices of non-zero values
print(e)

f = np.mean(np.random.random((30)))
print(f)

g = np.ones((3,3))
g[1,1] = 0
print(g)

h = np.zeros((8,8))
h[0::2,1::2] = 1
h[1::2,0::2] = 1
print(h)

i1 = np.array([0, 1])
i2 = i1[::-1]
i = np.tile([i1,i2],(4,4)) #checkboard with np.tile
print(i)

j = np.arange(11)
j[np.logical_and(j > 3,j < 8)] *= -1 
print(j)

k = np.sort(np.random.random(10))
print(k)

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
l = np.array_equal(A,B)
print(l)

Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)

A = np.arange(9).reshape(3,3)
B = A + 1
n = np.diag(np.dot(A,B))
print(n)



