# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    path="C:/Users/Danish/Desktop/DIVP/Images/eye1.jpg"
    img = cv2.imread(path,0)
    plt.hist(img.ravel(),255,[0,255])
    plt.show()
    
    #thresholding: 2nd arg= threshold value, 3rd arg=max value to be given to pixel above threshold
    thr=int(input("Enter the threshold: "))
    ret,thresh = cv2.threshold(img,thr,255,cv2.THRESH_BINARY)
    

    
    '''
    imghist=plt.hist(img.ravel(),255,[0,255])
    threshimg=plt.hist(thresh.ravel(),255,[0,255])
    '''
    
    plt.subplot(1,2,1),plt.imshow(img,'gray')
    plt.title('Original Image')
    plt.xticks([]),plt.yticks([])
    
    plt.subplot(1,2,2),plt.imshow(thresh,'gray')
    plt.title('Global Threshold Image')
    plt.xticks([]),plt.yticks([])
    '''
    plt.subplot(2,2,3),plt.imshow(imghist,'gray')
    plt.title('GLobal Threshold Image')
    plt.xticks([]),plt.yticks([])
    
    plt.subplot(2,2,4),plt.imshow(imghist,'gray')
    plt.title('GLobal Threshold Image')
    plt.xticks([]),plt.yticks([])
'''
    plt.show()
  
    
main()

