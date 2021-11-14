# -*- coding: utf-8 -*-
import cv2
import numpy as np

# read image
path="C:/Users/Danish/Desktop/DIVP/Images/eye2.jpg"
img = cv2.imread(path, 0)

# normalize float versions
norm_img1 = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
norm_img2 = cv2.normalize(img, None, alpha=0, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

# scale to uint8
norm_img1 = (255*norm_img1).astype(np.uint8)
norm_img2 = np.clip(norm_img2, 0, 1)
norm_img2 = (255*norm_img2).astype(np.uint8)

# display input and both output images
cv2.imshow('original',img)
cv2.imshow('normalized1',norm_img1)
cv2.imshow('normalized2',norm_img2)
cv2.waitKey(0)
cv2.destroyAllWindows(30000)