# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt

#add, subtract
def arith_op(img1,img2):
   img3=cv2.add(img1,img2)
   img4=cv2.subtract(img1,img2)
   cv2.imshow('initial img1',img1)
   cv2.waitKey(50)
   cv2.imshow('initial img2',img2)
   cv2.waitKey(100)
   cv2.imshow('add result',img3)
   cv2.waitKey(150)
   cv2.imshow('sub result',img4)
   if cv2.waitKey(0) & 0xff == 27:
       cv2.destroyAllWindows()

#and, or, exor
def logic_op(img1,img2):
   img3=cv2.bitwise_and(img1,img2)
   img4=cv2.bitwise_or(img1,img2)
   img5=cv2.bitwise_xor(img1,img2)
   cv2.imshow('initial img1',img1)
   cv2.waitKey(500)
   cv2.imshow('initial img2',img2)
   cv2.waitKey(250)
   cv2.imshow('and result',img3)
   cv2.waitKey(100)
   cv2.imshow('or result',img4)
   cv2.waitKey(50)
   cv2.imshow('xor result',img5)
   cv2.waitKey(0)

def main():
    path1="C:/Users/Danish/Desktop/DIVP/bnw/bwsplit2.png"
    img1 = cv2.imread(path1,0)
    path2="C:/Users/Danish/Desktop/DIVP/bnw/bwsplit.png"
    img2 = cv2.imread(path2,0)
    arith_op(img1,img2)
    #logic_op(img1,img2)

main()
