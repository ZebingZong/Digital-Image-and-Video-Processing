import numpy as np 

# Construct the matrix
input = np.matrix([[2, 1, 0, 1], [1, 0, 0, 0], [1, 0, 0, 0]])

# Calculate DFT
output = np.fft.fft2(input)

print output
