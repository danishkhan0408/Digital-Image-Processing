# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

def pseudoColor(img,row,col):
    img1 = np.zeros(shape=(row,col,3) ,dtype = 'uint8')
    for i in range(row):
        for j in range(col):
            if img[i,j]>0and img[i,j]<50:
                img1[i,j,0] = img[i,j]+125
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]
            elif img[i,j]>50 and img[i,j]<100:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]+125
                img1[i,j,2] = img[i,j]
            elif img[i,j]>100 and img[i,j]<150:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]+155
            elif img[i,j]>150 and img[i,j]<200:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]+125
            elif img[i,j]>200 and img[i,j]<215:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]+200
            elif img[i,j]>215 and img[i,j]<225:
                img1[i,j,0] = img[i,j]+255
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]
            elif img[i,j]>225 and img[i,j]<235:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]+255
                img1[i,j,2] = img[i,j]
            elif img[i,j]>235 and img[i,j]<245:
                img1[i,j,0] = img[i,j]
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]+255
            else:
                img1[i,j,0] = img[i,j]+255
                img1[i,j,1] = img[i,j]
                img1[i,j,2] = img[i,j]
    return img1

def main():
    img = cv2.imread('C:/Users/Danish/Desktop/DIVP/Images/penguin.jpg',0) 
    rows,cols=img.shape
    newimg=pseudoColor(img, rows, cols)    

    fig = plt.figure(figsize=(30, 18))
    grid = plt.GridSpec(2, 2, wspace=0.2, hspace=0.5)
                        
    plt.subplot(2, 3, 1), plt.imshow(img, 'gray')
    plt.subplot(2, 3, 2), plt.imshow(newimg, 'gray')

    plt.subplot(2, 3, 4),plt.hist(img.ravel(),256,[0,256])
    color = ('b', 'g', 'r')
    plt.subplot(2, 3, 5)
    for i, col in enumerate(color): 
        histr = cv2.calcHist([newimg], [i], None, [256], [0, 256]) 
        plt.plot(histr, color = col) 
        plt.xlim([0, 256]) 
    plt.show()

main()
