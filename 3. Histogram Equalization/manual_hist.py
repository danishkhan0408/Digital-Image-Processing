# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:14:58 2020

@author: Danish
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt 

def manHist(img):
   row, col = img.shape # img is a grayscale image
   y = np.zeros((256), np.uint64)
   for i in range(0,row):
      for j in range(0,col):
         y[img[i,j]] += 1
   x = np.arange(0,256)
   plt.bar(x,y,color="gray",align="center")
   plt.show()

def hist_plot(img):
   #plot histogram
   plt.hist(img.ravel(),255,[0,255])
   plt.show()
   
def main():
   path="C:/Users/Danish/Desktop/DIVP/Images/flower.jpg"
   img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
   manHist(img)
   hist_plot(img)
   
main()

