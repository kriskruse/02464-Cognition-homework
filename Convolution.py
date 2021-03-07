import numpy as np


#I = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
I = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])
w = 0.1
F = np.array([-w , 1, -w])

print(np.convolve(I,F))
print(len(np.convolve(I,F)))