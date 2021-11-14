# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:25:34 2020

@author: Danish
"""
import matplotlib.pyplot as plt
import cv2
import numpy as np

def Erosion(padImg, kernel, size,rows,cols):
    output = np.zeros((rows, cols), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, cols):
            # Slicing
            portion = padImg[i:i+size, j:j+size]
            # sum of Kernel and window
            portion1 = portion.flatten()
            portion2 = kernel.flatten()
            p1 = (np.sum(portion1))
            p2 = (np.sum(portion2))*255
            # if Fit Condition Satisfies
            if p1 == p2:
                output[i, j] = 255
            else:
                output[i, j] = np.min(portion1)
    return output
def Dilation(img, size,rows,cols):
    output = np.zeros((rows, cols), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, cols):
            portion = img[i:i+size, j:j+size]
            portion = portion.flatten()
            # Apply dilation
            if 255 in portion:
                output[i, j] = 255
            else:
                output[i, j] = 0
    return output

def opening(img,kernel):
    ero_img = cv2.erode(img, kernel, iterations=1)
    out = cv2.dilate(ero_img, kernel, iterations=1)
    return out

def closing(img,kernel):
    dil_img = cv2.dilate(img, kernel, iterations=1)
    out = cv2.erode(dil_img, kernel, iterations=1)
    return out
   
def main():
    path="C:/Users/Danish/Desktop/DIVP/Images/morph1.bmp"
#    path="C:/Users/Danish/Desktop/DIVP/Images/morph3.png"
    img = cv2.imread(path,0) 
    size = 3
    # Structuring Element
    kernel = np.ones((size, size), np.uint8)
    open_size = 35
    close_size = 22
    # Structuring Element along with the size 
    open_kernel = np.ones((open_size, open_size), np.uint8)
    close_kernel = np.ones((close_size, close_size), np.uint8)

    # getting size of image
    rows= img.shape[0]
    cols = img.shape[1]
    # Dilation & erosion
    dilated_img = Dilation(img, size,rows,cols)
    erosion_img = Erosion(img, kernel, size,rows,cols)
    inbuilt_dilation = cv2.dilate(img, kernel, iterations=1)
    inbuilt_erosion = cv2.erode(img, kernel, iterations=1)
    out=cv2.hconcat([img,dilated_img,erosion_img])
    
    '''
    open_img=opening(img,open_kernel)
    close_img=closing(img,close_kernel)
    
    out=cv2.hconcat([img,open_img,close_img])
    '''
      
    cv2.imshow('output',out)
    cv2.waitKey(300000)
    cv2.destroyAllWindows()

main()
