import cv2
import numpy as np
from scipy.signal import convolve2d


def kernel(N, w):
    F = np.ones([N, N])
    F = np.pad(F, N, 'constant', constant_values=-w)
    return F


img = cv2.imread("MonaLisa.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = cv2.normalize(gray.astype('float'), None, 0.0, 1.0, cv2.NORM_MINMAX)
w = 0.1

print(kernel(4, w))

convimg = convolve2d(out, kernel(10, w))

cv2.imshow("out", convimg)
cv2.imshow("original", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
