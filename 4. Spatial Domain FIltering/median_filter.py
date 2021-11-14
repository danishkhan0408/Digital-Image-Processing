# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:53:45 2020

@author: Danish
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def padding(originalImg, padSize,rows,columns):
    padImg = np.zeros((rows+2*padSize, columns+2*padSize), dtype=np.uint8)
    # Using Splicing
    padImg[padSize:rows+padSize, padSize:columns+padSize] = originalImg
    return padImg

def MinFilter(padImg, size, rows, columns):
    output = np.zeros((rows, columns), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, columns):
            # using Splicing
            portion = padImg[i:i+size, j:j+size]
            
            # Converting Matrix to Array
            array1 = portion.flatten()
            Minv = np.min(array1)
            output[i][j] = Minv
    return output

def MaxFilter(padImg, size, rows, columns):
    output = np.zeros((rows, columns), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, columns):
            # using Splicing
            portion = padImg[i:i+size, j:j+size]
            # Converting Matrix to Array
            array1 = portion.flatten()
            Minv = np.max(array1)
            output[i][j] = Minv
    return output

def MedianFilter(padImg, size,rows, columns):
    output = np.zeros((rows, columns), dtype=np.uint8)
    for i in range(0, rows):
        for j in range(0, columns):
            # using Splicing
            portion = padImg[i:i+size, j:j+size]
            # Converting Matrix to Array
            array1 = portion.flatten()
            medianv = np.lib.median(array1)
            output[i][j] = medianv
    return output

def inbuiltMedianFilter(img,n):
    blurImg = cv2.medianBlur(img,n)
    return blurImg 

def inbuiltMinFilter(img,n):
    size = (n, n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    minImg = cv2.erode(img, kernel)
    return minImg

def inbuiltMaxFilter(img,n):
    size = (n,n)
    shape = cv2.MORPH_RECT
    kernel = cv2.getStructuringElement(shape, size)
    minImg = cv2.dilate(img, kernel)
    return minImg

   
def hist_plot(histimg1,histimg2,histimg3):
   #plot histogram
   plt.subplot(131),plt.hist(histimg1.ravel(),255,[0,255]),plt.title('Original')
   plt.xticks([]), plt.yticks([])
   plt.subplot(132),plt.hist(histimg2.ravel(),255,[0,255]),plt.title('Manual Filter')
   plt.xticks([]), plt.yticks([])
   plt.subplot(133),plt.hist(histimg3.ravel(),255,[0,255]),plt.title('Inbuilt Filter')
   plt.xticks([]), plt.yticks([])
   plt.show()
    
def main():
    path="C:/Users/Danish/Desktop/DIVP/Images/saltimage.jpg"
    img = cv2.imread(path,0) 
    
    size=3 #mask size
    pad_size= size//2
    rows = img.shape[0]
    columns = img.shape[1]
    padImg = padding(img, pad_size,rows,columns)
    
    op=input("1. Median Filter\n2. Min Filter\n3. Max Filter\n")
    if op == 1:
        img2=MedianFilter(padImg, size, rows, columns)
        img3=inbuiltMedianFilter(img,size)
    elif op == 2:
        img2=MinFilter(img, size, rows, columns)
        img3=inbuiltMinFilter(img,size)
    else:
        img2=MaxFilter(padImg, size, rows, columns)
        img3=inbuiltMaxFilter(img,size)
    
    hist_plot(img,img2, img3)
    out=cv2.hconcat([img,img2,img3])
    cv2.imshow('output',out)
    cv2.waitKey(300000)
    cv2.destroyAllWindows()

main()
