from scipy import ndimage
from scipy import misc
from math import log10
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# define the function to calculate PSNR
def calculatePSNR(img1, img2):
	# calculate MSE
	mse = 0
	for i in range(img1.shape[0]):
		for j in range(img1.shape[1]):
			diff = img1[i][j] - img2[i][j]
			mse += diff * diff

	mse = mse / (img1.shape[0] * img1.shape[1])
	# calculate PSNR
	MAX = 255
	psnr = 10 * log10(MAX * MAX / mse)
	return psnr

# Read image
img_noisy = misc.imread('noisy.jpg')
img_orig = misc.imread('original.jpg')
# Convert uint8 to float
img_noisy = img_noisy.astype(float)
img_orig = img_orig.astype(float)
# Perform a first-pass 3x3 uniform_filting
denoise1 = ndimage.median_filter(img_noisy, size=3, mode='constant')
# Perform a second-pass 3x3 uniform_filting
denoise2 = ndimage.median_filter(denoise1, size=3, mode='constant')

print calculatePSNR(img_orig, img_noisy)
print calculatePSNR(img_orig, denoise1)
print calculatePSNR(img_orig, denoise2)

# Show the image
fig = plt.figure()
fig.add_subplot(2, 2, 1)
plt.imshow(img_orig, cmap = cm.Greys_r)
fig.add_subplot(2, 2, 2)
plt.imshow(img_noisy, cmap = cm.Greys_r)
fig.add_subplot(2, 2, 3)
plt.imshow(denoise1, cmap = cm.Greys_r)
fig.add_subplot(2, 2, 4)
plt.imshow(denoise2, cmap = cm.Greys_r)
plt.show()





# # Calcuate MSE
# mse1 = 0 
# mse2 = 0
# for i in range(lena.shape[0]):
# 	for j in range(lena.shape[1]):
# 		diff1 = lena[i][j] - blurred1[i][j]
# 		diff2 = lena[i][j] - blurred2[i][j]
# 		mse1 += diff1 * diff1
# 		mse2 += diff2 * diff2

# mse1 = mse1 / (lena.shape[0] * lena.shape[1])
# mse2 = mse2 / (lena.shape[0] * lena.shape[1])

# # Calcuate PSNR
# MAX = 255
# psnr1 = 10 * log10(MAX * MAX / mse1)
# psnr2 = 10 * log10(MAX * MAX / mse2)

# print psnr1 
# print psnr2


