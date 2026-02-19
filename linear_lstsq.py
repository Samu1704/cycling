import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt

matrix = np.array([ [81.9, 720],
                    [42.4, 180],
                    [19.5, 280],
                    [164, 1200]
                    ])

rhs = np.array([246, 120, 61, 564])

p, res, rnk, s = scipy.linalg.lstsq(matrix, rhs)
print(p)
print(matrix@p-rhs)