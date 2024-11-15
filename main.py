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
def matrix_minor(m, c, r):
	maxN = m.shape[1]

	r-=1
	c-=1

	return np.vstack((np.hstack((m[0:r, 0:c], m[0:r, c+1:maxN])), np.hstack((m[r+1:maxN, 0:c], m[r+1:maxN, c+1:maxN]))))

def matrix_det(m):
	det = 0

	#base case
	if m.shape[0] == 2 and m.shape[1] == 2:
		return (m[0, 0]*m[1, 1]) - (m[1, 0]*m[0, 1])

	for i in range(1, m.shape[0]+1):
		det += matrix_det(matrix_minor(m, 1, i))

	return det

# Determinate must be nonzero and not divisible by 2 or 13
def matrix_valid(m):
	det = matrix_det(m)

	if det != 0 and det%2!=0 and det%26!=0:
		return True
	return False

#m matrix
#pt plain text
#only works for 3x3 matrix's
def hill_cipher(m, pt):
	maxN = m.shape[1]
	arr = []
	sArr = []

	#split plain text into slices that are the size of one dimension of the matrix
	for i in range(0, len(pt), maxN):
		#loop through each character 
		for j in range(i, i+maxN):
			currChar = pt[j:j+1]
			
			if currChar == ' ' or currChar == '':
				currChar = '0'
			
			arr.append(ord(currChar))

		print(np.array([[arr[0]], [arr[1]], [arr[2]]]))
		print(m * np.array([[arr[0]], [arr[1]], [arr[2]]]))

		arr = []
		

	return sArr




#m matrix
#cp cipher text
#def hill_cipher_decode(m, cp)

if __name__ == '__main__':
	#gen a random matrix
	matrix = matrix_gen(3)

	#generate matrix's until finding a valid one
	while matrix_valid(matrix) != True:
		matrix = matrix_gen(3)

	#input string

	#do hill cipher
	print(matrix)
	print(hill_cipher(matrix, "hello world"))