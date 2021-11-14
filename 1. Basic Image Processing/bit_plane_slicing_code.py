# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:18:28 2020

@author: Danish
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(img):
    out = []
    for k in range(0, 9):
        
        # create an image for the k bit plane
        plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
        # execute bitwise and operation
        res = cv2.bitwise_and(plane, img)
        # multiply ones (bit plane sliced) with 255 just for better visualization
        x = res * 255
        # append to the output list
#        out.append(x)
#        outfinal = np.hstack(out)
        cv2.imshow("bit plane", x)
        cv2.waitKey()    
def main():
   path="C:/Users/Danish/Desktop/DIVP/Images/flower.jpg"
   img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
   bit_plane_slicing(img)      

main()








