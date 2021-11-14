# -*- coding: utf-8 -*-
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Image read
#path = "C:/Users/Danish/Desktop/DIVP/presentation/einstein.jpg"
img = Image.open(r"F:/be_project/RAW_images/disc1/OAS1_0001_MR1/RAW/img.gif")
#img = cv2.imread(path, 0)
#img = cv2.resize(img, (500, 500))
#cv2.imshow('img', img)
#cv2.waitKey(0)

size = 256
# Cut off Frequency


Do = 50
# High pass Filter using Distance Matrix
def FilterDesign(img, size, Do):
    # D is distance Matrix
    D = np.zeros([size, size], dtype=np.uint32)
    # H is Filter
    H = np.zeros([size, size], dtype=np.uint8)
    #r = img.shape[0] // 2
    #c = img.shape[1] // 2
    r = 256//2
    c = 256//2
    # Distance Vector
    for u in range(0, size):
        for v in range(0, size):
            D[u, v] = abs(u - r) + abs(v - c)
    # Using Cut off frequncy applying 0 and 255 in H to make a High Pass Filter and center = 1
    for i in range(size):
        for j in range(size):
            if D[i, j] > Do:
                H[i, j] = 255
            else:
                H[i, j] = 0
    return H
# High Pass Filter
H = FilterDesign(img, size, Do)
#cv2.imshow('Rectangular High Pass Filter', H)
#cv2.waitKey(3000)
#cv2.destroyAllWindows()
# Applying fft and shift
input = np.fft.fftshift(np.fft.fft2(img))
# Multiplying image with Low Pass Filter
out = input*H
# Taking Inverse Fourier of image
out = np.abs(np.fft.ifft2(np.fft.ifftshift(out)))
out = np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX, -1))
# Gradient image after applying High pass filter
cv2.imshow('High Pass Filtered Image', out)
cv2.waitKey(30000)#30 secs
cv2.destroyAllWindows()
