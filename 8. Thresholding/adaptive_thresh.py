# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np

path="C:/Users/Danish/Desktop/DIVP/Images/eye2.jpg"
img = cv2.imread(path,0)


# applying different thresholding
# techniques on the input image
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 19, 3)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 19, 3)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input image
cv2.imshow('Adaptive Mean', thresh1)
cv2.imshow('Adaptive Gaussian', thresh2)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
