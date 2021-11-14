# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

#add, or
def compare_op(img1,img2):
   img3=cv2.add(img1,img2)
   img4=cv2.bitwise_or(img1,img2)
   cv2.imshow('initial img1',img1)
   cv2.waitKey(500)
   cv2.imshow('initial img2',img2)
   cv2.waitKey(250)
   cv2.imshow('add result',img3)
   cv2.waitKey(100)
   cv2.imshow('or result',img4)
   cv2.waitKey(0)

def main():
    path1="C:/Users/Danish/Desktop/DIVP/bnw/chess.png"
    img1 = cv2.imread(path1,0)
    path2="C:/Users/Danish/Desktop/DIVP/bnw/chess2.png"
    img2 = cv2.imread(path2,0)
    compare_op(img1,img2)

main()
