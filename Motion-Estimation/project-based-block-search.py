# using three fast matching error measures based on the integral projections
# vertical projections(column sum), horizontal projections(row sum), massive projections(block sum)
# the three error measures have simple complexity and help to reject candidate blocks

import sys
from scipy import misc
from numpy import *
import time

# Read image
frame1 = misc.imread("frame_1.jpg")
frame2 = misc.imread("frame_2.jpg")

# Convert uint8 to float
frame1 = frame1.astype(float)
frame2 = frame2.astype(float)
(row, col) = frame1.shape

# Get the reference and target block
block_ref = frame1[64:96, 80:112]
block_tar = frame2[64:96, 80:112]
size = block_tar.shape[0]

# The starting point of main algorithm
start_time = time.time()

# Initialize minSAE, min_posI, min_posJ 
# Calculate rowSum_tarF, colSum_tarF, bSum_tarF, 'F' means 'fixed'
min_SAE = 0
bSum_tarF = 0
rowSum_tarF = zeros(size, int) 
colSum_tarF = zeros(size, int)
min_posI = 64
min_posJ = 80

for i in range(size):
	for j in range(size):
		# Calculate row-sums of block_tar
		rowSum_tarF[i] += block_tar[i][j]
		# Calculate col-sums of block_tar
		colSum_tarF[j] += block_tar[i][j]
		# Calculate block-sums of block_tar
		bSum_tarF += block_tar[i][j]
		# Initialize minSAE
		min_SAE += abs(block_tar[i][j] - block_ref[i][j])

# Initialize the row-sums of reference frame buffer with leftside values
rowSum_ref_buffer = zeros(row, int)
for i in range(row):
	for j in range(size):
		rowSum_ref_buffer[i] += frame1[i][j]

# Initialize the col-sums of reference frame buffer with topside values
colSum_ref_buffer = zeros(col, int)
for j in range(col):
	for i in range(size):
		colSum_ref_buffer[j] += frame1[i][j]

rowSum_ref = zeros(size, int)
colSum_ref = zeros(size, int)

for refRange_i in range(row - size + 1):

	# Initialize row-sums of macroblock of reference
	for i in range(size):
		rowSum_ref[i] = rowSum_ref_buffer[i + refRange_i]

	# Update col-sums of buffer of reference if refRange_i >= 1
	if(refRange_i >= 1):
		for j in range(col):
			colSum_ref_buffer[j] += (frame1[refRange_i + size - 1][j] - frame1[refRange_i - 1][j])


	for refRange_j in range(col - size + 1):

		# Update col-sums and block-sums of macroblock of reference
		bSum_ref = 0
		for j in range(size):
			colSum_ref[j] = colSum_ref_buffer[j + refRange_j]
			bSum_ref += colSum_ref[j]

		# Update row-sums of macroblock in reference if refRange_j >= 1
		if(refRange_j >= 1):
			for i in range(size):
				rowSum_ref[i] += (frame1[refRange_i + i][refRange_j + size - 1] - frame1[refRange_i + i][refRange_j - 1])

		# Calculate the horizontal error measures
		sae = 0
		for i in range(size):
			sae += abs(rowSum_ref[i] - rowSum_tarF[i])
		if sae >= min_SAE:
			continue

		# Calculate the vertical error measures
		sae = 0
		for j in range(size):
			sae += abs(colSum_ref[j] - colSum_tarF[j])
		if sae >= min_SAE:
			continue

		# Calculate the massive error measures
		sae = abs(bSum_ref - bSum_tarF)
		if sae >= min_SAE:
			continue

		# Calculte the SAE between the target block and the candidate block in reference
		block_ref = frame1[refRange_i:refRange_i+size, refRange_j:refRange_j+size]
		sae = 0
		for i in range(size):
			for j in range(size):
				sae += abs(block_tar[i][j] - block_ref[i][j])
		if sae < min_SAE:
			min_posI = refRange_i
			min_posJ = refRange_j
			min_SAE = sae

print ("--- %s seconds ---" % (time.time() - start_time))
print min_posI
print min_posJ
print min_SAE/32/32



