# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:20:33 2020

@author: Danish
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the Image
path = 'C:/Users/Danish/Desktop/DIVP/Images/puppy.jpg'
img = cv2.imread(path,0)

# Histogram of Image
hist,bins = np.histogram(img.flatten(),256,[0,256])

# Equalizing the Image [In-Built Command]
equ_img = cv2.equalizeHist(img)
cv2.imwrite('In-built_Hist_Eq.png',equ_img)
cv2.imshow('Equalized Image',equ_img)
cv2.waitKey(300000) 
cv2.destroyAllWindows()
# Calculating CDF
cdf = hist.cumsum()
cdf_norm1 = cdf *( hist.max()/ cdf.max())

# Displaying Input image and Histogram
cv2.imshow('Input Image',img)
cv2.waitKey(300000) 
cv2.destroyAllWindows()
plt.plot(cdf_norm1, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

# Equalizing the Image Histogram
cdf_temp = np.ma.masked_equal(cdf,0)
cdf_temp = (cdf_temp - cdf_temp.min())*255/(cdf_temp.max()-cdf_temp.min())
cdf_eq = np.ma.filled(cdf_temp,0).astype('uint8')
img2 = cdf_eq[img]

# Equalized Image Histogram
hist,bins = np.histogram(img2.flatten(),256,[0,256])

# Equalized Image CDF
cdf2 = hist.cumsum()
cdf2_norm2 = cdf2 *( hist.max()/ cdf2.max())

# Displayng Output Image and Histogram
cv2.imshow('Histogram Equalized image',img2)
cv2.waitKey(300000) 
cv2.destroyAllWindows()
plt.plot(cdf2_norm2, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

