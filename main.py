import numpy as np
from numpy.random import default_rng
import random as rng

#generate a random matrix
def matrix_gen(n):
	matrix = default_rng(round(rng.random()*10000)).random((n,n))

	for a in range(0, len(matrix)):
		for b in range(0, len(matrix)):
			matrix[a][b] = int(round(matrix[a][b]*10))

	return matrix

# Get the minor of a matrix
def matrix_minor(m, r, c):
	maxN = m.shape[1]

	r-=1
	c-=1

	return np.vstack((np.hstack((m[0:r, 0:c], m[0:r, c+1:maxN])), np.hstack((m[r+1:maxN, 0:c], m[r+1:maxN, c+1:maxN]))))

# Determinate must be nonzero and not divisible by 2 or 13
#def matrix_valid(m):


if __name__ == '__main__':
	matrix = matrix_gen(2)

	print(matrix)
	print(matrix_minor(matrix, 1, 1))