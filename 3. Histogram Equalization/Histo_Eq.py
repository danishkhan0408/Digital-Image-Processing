# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histoEQ( imgeq ):
    rows=imgeq.shape[0]
    cols=imgeq.shape[1]
    out=np.zeros((rows,cols),np.uint64)
    new_gray_level=np.zeros((256),np.uint64)
    for i in range(rows):
        for j in range(cols):
            out[imgeq[i,j]] +=1
    total= cols*rows
    curr=0
    for i in range(0,256):
        curr += out[i];
        new_gray_level[i] = round(curr*255/total)
    for i in range(0,rows):
        for j in range(0,cols):
            imgeq[j]=new_gray_level[imgeq[j]]
     
    return imgeq
      
                
    #plt.subplot(2,1,1) , plt.imshow(imgeq) , plt.title('Equilized IMG')
    #plt.subplot(2,1,1) , plt.imshow(histogram(imgeq)) , plt.title('Equilized Histogram')

#def HistoEQ(imgeq):
#    row,col = imgeq.shape
#    x=np.zeros((256,),dtype=np.float16)
#    y=np.zeros((256,),dtype=np.float16)
#    for i in range(0,row):
#        for j in range(0,col):
#            x[imgeq[i,j]] +=1
#    print(x)
#    a=255/(row*col)
#    y[0] = x[0]*a
#    for i in range (1,256):
#        y[i]=y[i-1] + x[i]*a
#    for i in range (1,256):
#        y[i]=round(y[i])
#    b = np.array(y,dtype=np.uint8)
#    print(b)
#    im=np.zeros((row,col),dtype=np.uint8)
#    for i in range(0,row):
#        for j in range(0,col):
#            g=imgeq[j,i]
#            im[j,i]=y[g]
#    plt.subplot(2,1,1) , plt.imshow(im) , plt.title('Equilized IMG')
#    plt.subplot(2,1,1) , plt.imshow(histogram(im)) , plt.title('Equilized Histogram')

#plt.hist(img.flatten(),256,[0,256],color = 'r')
#plt.show() 
def main(): 
    img = cv2.imread('C:/Users/Danish/Desktop/DIVP/Images/dk.jpg') 
    #histogram(img)
    equ = cv2.equalizeHist(img) 
    #histogram(equ)
    #man_eq=histoEQ(img)
    
    #out=cv2.hconcat([img,equ,man_eq])
    out=cv2.hconcat([img,equ])
 
    path_out = "C:/Users/Danish/Desktop/DIVP/Images/"
    img_path_out = path_out + 'filtered.jpg'
    cv2.imwrite(img_path_out, out)
    
'''   
    cv2.imshow('EquilizedImage', out)
    cv2.waitKey(300000) 
    cv2.destroyAllWindows()
''' 

main()
