# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:01:54 2020

@author: Danish
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    path="C:/Users/Danish/Desktop/DIVP/Images/lenna.jpg"
    img = cv2.imread(path,0)
    
    kernelx = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    kernely = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    sobel_img_x = cv2.filter2D(img, -1, kernelx)
    sobel_img_y = cv2.filter2D(img, -1, kernely)
    sobel_img=sobel_img_x+sobel_img_y
    
    kernel1x = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    kernel1y = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    prewitt_img_x = cv2.filter2D(img, -1, kernel1x)
    prewitt_img_y = cv2.filter2D(img, -1, kernel1y)    
    prewitt_img = prewitt_img_x+prewitt_img_y

    kernel2x = np.array([[-1,0],[0,-1]])
    kernel2y = np.array([[0,-1],[1,0]])
    robert_img_x = cv2.filter2D(img, -1, kernel2x)
    robert_img_y = cv2.filter2D(img, -1, kernel2y)    
    robert_img = robert_img_x+robert_img_y
    
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(sobel_img,cmap = 'gray')
    plt.title('Sobel'), plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(prewitt_img,cmap = 'gray')
    plt.title('Prewitt'), plt.xticks([]),plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(robert_img,cmap = 'gray')
    plt.title('Robert'), plt.xticks([]),plt.yticks([])
    plt.show()

main()
