# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np

path="C:/Users/Danish/Desktop/DIVP/Images/eye2.jpg"
img = cv2.imread(path,0)
plt.hist(img.ravel(),256,[0,256])
plt.show()

# applying different thresholding
# techniques on the input image
# all pixels value above 250 will
# be set to 255
ret, thresh1 = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)

row, column = img.shape
img1 = np.zeros((row,column))

for i in range(row):
    for j in range(column):
        if img[i, j] >= 250:
            img1[i, j] = 255
        else:
            img1[i,j] = 0


cv2.imshow('Input Image', img)
cv2.imshow('Inbuilt Binary Thresholded', thresh1)
cv2.imshow('Binary Thresholded', img1)
cv2.imshow('Binary Threshold Inverted', thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()
