# -*- coding: utf-8 -*-
import cv2
import numpy as np

def low_pass(img):
    #filter design
    Do = 50 #value of Cutoff freq Do
    ham = np.hamming(500)[:,None] # 1D hamming
    ham2d = np.sqrt(np.dot(ham, ham.T)) ** Do # expand to 2D hamming

    #Transforming the image to freq domain, output has 2 parts: real and imaginary
    f = cv2.dft(img.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
    #Since the center of image does not coincide with the origin
    #we have to handle this problem with np.fft.fftshift() function
    #What this function does is just divide an image into four small images
    #and then rearrange them such that it becomes symmetric about the center.
    f_shifted = np.fft.fftshift(f)
    f_complex = f_shifted[:,:,0]*1j + f_shifted[:,:,1]

    #applying the filter to the image
    f_filtered = ham2d * f_complex

    #taking inverse FT
    f_filtered_shifted = np.fft.fftshift(f_filtered)
    
    cv2.imshow('output',img)
    cv2.waitKey(30000)#30 secs
    cv2.destroyAllWindows()
    
    inv_img = np.fft.ifft2(f_filtered_shifted)
    filtered_img = np.abs(inv_img)
    filtered_img -= filtered_img.min()
    #expand the result such that all values are between 0 and 255
    filtered_img = filtered_img*255 / filtered_img.max()
    #convert back to uint8
    filtered_img = filtered_img.astype(np.uint8)
    final_img=cv2.hconcat([img,filtered_img])
    display_img(final_img)

def display_img(img):

    cv2.imshow('output',img)
    cv2.waitKey(30000)#30 secs
    cv2.destroyAllWindows()

def main():
    path = "C:/Users/Danish/Desktop/DIVP/presentation/einstein.jpg"
    img = cv2.imread(path,0) # gray-scale image
    img = img[:500, :500] # crop to 500 x 500 
    low_pass(img)
    
main()
