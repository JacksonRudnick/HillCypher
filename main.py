import numpy as np
from numpy.random import default_rng
import random as rng

if __name__ == '__main__':
    matrix = default_rng(round(rng.random()*10000)).random((3,3))

    for a in range(0, len(matrix)):
        print(a)
        for b in range(0, len(matrix)):
            print(b)
            matrix[a][b] = int(round(matrix[a][b]*10))