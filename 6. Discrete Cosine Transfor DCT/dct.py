# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:54:54 2020

@author: Danish
"""

from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    # Reading the input image
    path="C:/Users/Danish/Desktop/DIVP/Images/tajmahal1.jpg"
    img = cv2.imread(path, 0)
    
    imf = np.float32(img)/255.0  # float conversion/scale
    dct1 = cv2.dct(imf)              # the dct
    dct = np.uint8(dct1*255.0)    # convert back to int
    
    idct = cv2.idct(dct1)         # take idct
    
    error = imf - idct

    idct = np.uint8(idct*255.0)  #convert back to int
    error = np.uint8(error*255.0)


    plt.figure(0)
    plt.imshow(img, cmap=plt.cm.gray)
    plt.title('Original Image')

    plt.figure(1)
    plt.imshow(dct, cmap=plt.cm.gray)
    plt.title('DCT of Image')

    plt.figure(2)
    plt.hist(img.ravel() , bins=256)
    plt.title("Histogram of an original image")

    plt.figure(3)
    plt.hist(dct.ravel() , bins=256)
    plt.title("Histogram of DCT ")

    plt.figure(4)
    plt.imshow(idct , cmap=plt.cm.gray)
    plt.title("IDCT")

    plt.figure(5)
    plt.hist(idct.ravel() , bins=256)
    plt.title("Histogram of IDCT ")

    plt.figure(6)
    plt.imshow(error , cmap=plt.cm.gray)
    plt.title("Error between original and after taking IDCT")

main()