# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_trans(img):
    #log transform
    c = 255 / (np.log(1 + np.max(img)))
    log_trans_img= c * np.log(1 + img)
    log_trans_img = np.array(log_trans_img,dtype = np.uint8)

    img_concat_horizontal=np.concatenate((img,log_trans_img),axis=1)
    cv2.imshow('concatenated_horizontal',img_concat_horizontal)
    cv2.waitKey(0)
    #histogram of original image
    hist_plot(img)
    #histogram of log tranformed image
    hist_plot(log_trans_img)

def hist_plot(img):
   #plot histogram
   plt.hist(img.ravel(),255,[0,255])
   plt.show()
   
def main():
   path="C:/Users/Danish/Desktop/DIVP/Images/humm.jpg"
   img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
   log_trans(img)   

main()
