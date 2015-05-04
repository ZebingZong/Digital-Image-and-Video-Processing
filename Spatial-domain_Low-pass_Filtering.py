from scipy import ndimage
from scipy import misc
from math import log10

# Read image
lena = misc.imread('digital-images-week2_quizzes-lena.gif')
# Convert uint8 to float
lena = lena.astype(float)

# Perform 3x3 uniform_filting
blurred1 = ndimage.uniform_filter(lena, size=3, mode='nearest')
blurred2 = ndimage.uniform_filter(lena, size=5, mode='nearest')

# Calcuate MSE
mse1 = 0 
mse2 = 0
for i in range(lena.shape[0]):
	for j in range(lena.shape[1]):
		diff1 = lena[i][j] - blurred1[i][j]
		diff2 = lena[i][j] - blurred2[i][j]
		mse1 += diff1 * diff1
		mse2 += diff2 * diff2

mse1 = mse1 / (lena.shape[0] * lena.shape[1])
mse2 = mse2 / (lena.shape[0] * lena.shape[1])

# Calcuate PSNR
MAX = 255
psnr1 = 10 * log10(MAX * MAX / mse1)
psnr2 = 10 * log10(MAX * MAX / mse2)

print psnr1 
print psnr2


