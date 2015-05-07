import sys
import time
from scipy import misc

# Read image
frame1 = misc.imread("frame_1.jpg")
frame2 = misc.imread("frame_2.jpg")

# Convert uint8 to float
frame1 = frame1.astype(float)
frame2 = frame2.astype(float)
(row, col) = frame1.shape

# The starting point of main algorithm
start_time = time.time()

# Get the target block
block_target = frame2[64:96, 80:112]
(a, b) = block_target.shape

min_SAE = sys.float_info.max
min_i = -1
min_j = -1

for i in range(row - a):
	for j in range(col - b):
		block_compare = frame1[i:i+a, j:j+b]
		sum = 0
		for x in range(a):
			for y in range(b):
				sum += abs(block_target[x][y] - block_compare[x][y])
		if sum < min_SAE:
			min_i = i
			min_j = j
			min_SAE = sum

print ("--- %s seconds ---" % (time.time() - start_time))
print min_i
print min_j
print min_SAE/32/32



