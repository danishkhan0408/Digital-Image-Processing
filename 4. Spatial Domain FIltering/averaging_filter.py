# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:14:26 2020

@author: Danish
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def manual_laplacian_filter(img):
    mask = (np.array([-1, -1, -1,-1 ,8 ,-1,-1 ,-1 ,-1])).reshape(3,3)
    man_img = cv2.filter2D(img,-1,mask)
    return(man_img)

def manual_highboost_filter(img,k):
    mask = (np.array([-1, -1, -1,-1 ,k+8 ,-1,-1 ,-1 ,-1])).reshape(3,3)
    man_img = cv2.filter2D(img,-1,mask)
    return(man_img)

def manual_avg_filter(img):
    mask = np.ones((5,5),np.float32)/25 #9
    man_img = cv2.filter2D(img,-1,mask)
    return(man_img)

def manual_weighted_avg_filter(img):
    mask = (np.array([1, 2, 1,2 ,4 ,2,1 ,2 ,1])).reshape(3,3)
    mask=mask/16
    man_img = cv2.filter2D(img,-1,mask)
    return(man_img)


def inbuilt_avg_filter(img):
    blur_img = cv2.blur(img,(5,5))
    return(blur_img)

def hist_plot(histimg1,histimg2,histimg3,histimg4,histimg5):
   #plot histogram
   plt.subplot(231),plt.hist(histimg1.ravel(),255,[0,255]),plt.title('Original')
   plt.xticks([]), plt.yticks([])
   plt.subplot(232),plt.hist(histimg2.ravel(),255,[0,255]),plt.title('Box Filter')
   plt.xticks([]), plt.yticks([])
   plt.subplot(233),plt.hist(histimg3.ravel(),255,[0,255]),plt.title('Weighted Average Filter')
   plt.xticks([]), plt.yticks([])
   plt.subplot(234),plt.hist(histimg2.ravel(),255,[0,255]),plt.title('Laplacian Filter')
   plt.xticks([]), plt.yticks([])
   plt.subplot(235),plt.hist(histimg3.ravel(),255,[0,255]),plt.title('High Boost Filter')
   plt.xticks([]), plt.yticks([])
   plt.show()
    
def main():
    path="C:/Users/Danish/Desktop/DIVP/Images/lenna.jpg"
    img = cv2.imread(path,0)
    img2=manual_avg_filter(img)
   # img3=inbuilt_avg_filter(img)
    img3=manual_weighted_avg_filter(img)
    img4=manual_laplacian_filter(img)
    img5=manual_highboost_filter(img, 3) #A=3
    hist_plot(img, img2, img3,img4,img5)
    out=cv2.hconcat([img,img2,img3,img4,img5])
    cv2.imshow('output',out)
    cv2.waitKey(30000)
    cv2.destroyAllWindows()

main()
