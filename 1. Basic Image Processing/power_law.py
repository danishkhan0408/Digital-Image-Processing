# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt


def main():
    
    path="C:/Users/Danish/Desktop/DIVP/Images/humm.jpg"
    img = cv2.imread(path,0)
     
    for gamma in [0.1, 0.5, 1, 1.2, 2.2]: 
       # Apply gamma correction. 
       gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
       cv2.imshow('gamma transformed'+str(gamma), gamma_corrected)
       cv2.waitKey(0)
         
main()
