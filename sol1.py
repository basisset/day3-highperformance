#!/usr/bin/env python3

import numpy as np

#the letter of the array corresponds with the exercise

a = np.zeros(10)
a[4] = 1

b = np.arange(10,50)

c = b[::-1] #reversing a vector

d = np.reshape(np.arange(0,9), (3,3))

e = np.argwhere(np.array([1,2,0,0,4,0])) #finds indices of non-zero values

f = np.mean(np.random.random((30)))

g = np.ones((3,3))
g[1,1] = 0

h = np.zeros((8,8))
h[0::2,1::2] = 1
h[1::2,0::2] = 1

i1 = np.array([0, 1])
i2 = i1[::-1]
i = np.tile([i1,i2],(4,4)) #checkboard with np.tile

j = np.arange(11)
j[np.logical_and(j > 3,j < 8)] *= -1 

k = np.sort(np.random.random(10))




