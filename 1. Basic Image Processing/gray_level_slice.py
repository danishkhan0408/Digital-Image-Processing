# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
        
def grey_level_slicing(img,min_r,max_r,wbg):
    # Find width and height of image
    row, column = img.shape
    # Create an zeros array to store the sliced image
    img1 = np.zeros((row,column),dtype = 'uint8')
    # Specify the min and max range
    min_range = min_r
    max_range = max_r
    
    #with background
    if(wbg == 1):
        for i in range(row):
            for j in range(column):
                if img[i,j]>min_range and img[i,j]<max_range:
                    #object of interest becomes white, background reamins as it is
                    img1[i,j] = 255
                else:
                    img1[i,j]=img[i,j]
        display_img(img, img1)
                
    #without background
    elif(wbg == 2):
        # Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
        for i in range(row):
            for j in range(column):
                if img[i,j]>min_range and img[i,j]<max_range:
                    #object of interest becomes white
                    img1[i,j] = 255 
                else:
                    #background becomes black
                    img1[i,j] = 0
        display_img(img, img1)
    
    else:
        img2 = np.zeros((row,column),dtype = 'uint8')
        #with background
        for i in range(row):
            for j in range(column):
                if img[i,j]>min_range and img[i,j]<max_range:
                    #object of interest becomes white, background reamins as it is
                    img1[i,j] = 255
                else:
                    img1[i,j]=img[i,j]
        #without background            
        for i in range(row):
            for j in range(column):
                if img[i,j]>min_range and img[i,j]<max_range:
                    #object of interest becomes white
                    img2[i,j] = 255 
                else:
                    #background becomes black
                    img2[i,j] = 0
        display_img2(img, img1, img2)
       
    
def display_img(img,img1):
    # Display the image
    cv2.imshow('original image',img)
    cv2.waitKey(500)
    hist_plot(img)
    cv2.imshow('sliced image', img1)
    cv2.waitKey(0)
    hist_plot(img1)

def display_img2(img,img1,img2):
    # Display the image
    cv2.imshow('original image',img)
    cv2.waitKey(1000)
    hist_plot(img)
    cv2.imshow('with background', img1)
    cv2.waitKey(500)
    hist_plot(img1)
    cv2.imshow('without background', img2)
    cv2.waitKey(0)
    hist_plot(img2)
    
def hist_plot(img):
   #plot histogram
   plt.hist(img.ravel(),255,[0,255])
   plt.show()
   
def main():
   path="C:/Users/Danish/Desktop/DIVP/Images/flower.jpg"
   img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
   
   hist_plot(img)
   range1=int(input("Enter the lower intensity range: "))
   range2=int(input("Enter the higher intensity range: "))
   back=int(input("Gray Level Slicing methods:\n1. With Background\n2. Without background\n3. Both\n\nEnter your choice: "))
   grey_level_slicing(img,range1,range2,back)      

main()







