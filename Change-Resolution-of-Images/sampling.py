"""
Suppose the data in one axis is 1 2 3 4 5 6 7 8. 
The following table shows how the data is extended for each mode (assuming cval=0):

    mode       |   Ext   |         Input          |   Ext
    -----------+---------+------------------------+---------
    'mirror'   | 4  3  2 | 1  2  3  4  5  6  7  8 | 7  6  5
    'reflect'  | 3  2  1 | 1  2  3  4  5  6  7  8 | 8  7  6
    'nearest'  | 1  1  1 | 1  2  3  4  5  6  7  8 | 8  8  8
    'constant' | 0  0  0 | 1  2  3  4  5  6  7  8 | 0  0  0
    'wrap'     | 6  7  8 | 1  2  3  4  5  6  7  8 | 1  2  3
For an even window size n, consider the window of size n+1, and then don't include the lower and right edges. 
(The position of the window can be changed by using the origin argument.)
"""

from scipy import ndimage
from scipy import misc
from math import log10
import numpy as np

# Read image
img = misc.imread('digital-images-week3_quizzes-original_quiz.jpg')
# Convert uint8 to float
img = img.astype(float)

# Perform 3x3 uniform_filting
img_preprocess = ndimage.uniform_filter(img, size=3, mode='nearest')
# print img_preprocess
# print '--------------------------------------'

# Fill all odd-index row and column with zeros
row = img_preprocess.shape[0]
col = img_preprocess.shape[1]
for i in range(row):
	for j in range(col):
		if (i % 2 == 1) or (j % 2 == 1):
			img_preprocess[i][j] = 0

# print img_preprocess

# up_sampling using bilinear interpolation
kernal = np.array([[0.25, 0.5, 0.25], [0.5, 1, 0.5], [0.25, 0.5, 0.25]])
img_upSampling = ndimage.convolve(img_preprocess, kernal, mode='constant', cval=0.0)

# Calcuate MSE
mse = 0 
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		diff = img_upSampling[i][j] - img[i][j]
		mse += diff * diff

mse = mse / (img.shape[0] * img.shape[1])
# print mse
# Calcuate PSNR
MAX = 255
psnr = 10 * log10(MAX * MAX / mse)

print psnr


