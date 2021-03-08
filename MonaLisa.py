import numpy as np
import skimage.viewer
import cv2
from scipy.signal import convolve2d

# Settings
filename = "MonaLisa.jpg"
t = 0.3
w = 0.1

# Kernel creation function
def kernel(N, w):
    F = np.ones([N, N])
    F = np.pad(F, N, 'constant', constant_values=-w)
    return F

# Threshold apply function
def threshold(img, t):
    img[img < t] = 0
    return img


# Main data manipulation
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = cv2.normalize(gray.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)

# Test for kernel size 1 - 10
for N in range(10):
    convimg = convolve2d(out, kernel(N, w))
    convimg = threshold(convimg, t)
    viewer1 = skimage.viewer.ImageViewer(convimg)
    viewer1.show()
    print(N)


# Check size of arrays
# print(np.shape(img))
# print(np.shape(gray))


# display the image
# viewergray = skimage.viewer.ImageViewer(gray)
# viewergray.show()


