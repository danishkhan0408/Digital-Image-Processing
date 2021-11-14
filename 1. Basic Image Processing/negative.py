# -*- coding: utf-8 -*-
import cv2 
import matplotlib.pyplot as plt 
 
# Read an image 
path="C:/Users/Danish/Desktop/DIVP/Images/eye1.jpg"
img = cv2.imread(path,0) 
cv2.imshow('input image',img) 
cv2.waitKey(0)  
# Histogram plotting of original image 
plt.hist(img.ravel(),255,[0,255])
plt.show()  

# Negate the original image 
img_neg = 1 - img 
cv2.imshow('output image',img_neg) 
cv2.waitKey(0)  
# Histogram plotting of 
# negative transformed image 
plt.hist(img_neg.ravel(),255,[0,255])
plt.show()
