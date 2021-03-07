import sys
import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer
import cv2
from scipy.signal import convolve2d

# get filename, sigma, and threshold value from command line
filename = "MonaLisa.jpg"
sigma = 0.8
t = 0.5
w = 0.1


def kernel(N, w):
    F = np.ones([N, N])
    F = np.pad(F, N, 'constant', constant_values=-w)
    return F


def threshold(img, t):
    mask = img < t
    return mask


img = cv2.imread("MonaLisa.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = cv2.normalize(gray.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
convimg = convolve2d(out, kernel(10, w))

mask = convimg > t

# display the mask image
viewer1 = skimage.viewer.ImageViewer(mask)

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(img)
sel[mask] = img[mask]

# display the result
viewer2 = skimage.viewer.ImageViewer(sel)
viewer1.show()
viewer2.show()
