# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 20:53:33 2020

@author: Danish
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def getHSI(img):
        with np.errstate(divide='ignore', invalid='ignore'):
            bgr = np.float32(img) / 255
            blue = bgr[:, :, 0]
            green = bgr[:, :, 1]
            red = bgr[:, :, 2]
        def calc_intensity(red, blue, green):
            return np.divide(blue + green + red, 3)
        def calc_saturation(red, blue, green):
            minimum = np.minimum(np.minimum(red, green), blue)
            saturation = 1 - (3 / (red + green + blue + 0.001) * minimum)
            return saturation
        def calc_hue(red, blue, green):
            hue = np.copy(red)
            for i in range(0, blue.shape[0]):
                for j in range(0, blue.shape[1]):
                    hue[i][j] = 0.5 * ((red[i][j] - green[i][j]) + (red[i][j] - blue[i][j])) / \
                                math.sqrt((red[i][j] - green[i][j]) ** 2 +
                                          ((red[i][j] - blue[i][j]) * (green[i][j] - blue[i][j])))
                    hue[i][j] = math.acos(hue[i][j])

                    if blue[i][j] <= green[i][j]:
                        hue[i][j] = hue[i][j]
                    else:
                        hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]
            return hue

        # Merge channels into picture and return image
        hsi = cv2.merge(
            (calc_hue(red, blue, green), calc_saturation(red, blue, green), calc_intensity(red, blue, green)))
        return hsi


def getYIQ(img):
    # y=0.2989 * R + 0.5870 * G + 0.1140 * B
    # I=0.60*R - 0.28*G-0.32*B
    # Q=0.21*R -0.52*G+0.31*B
    YIQ = np.zeros([img.shape[0], img.shape[1], 3])
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            YIQ[i, j, 0] = 0.2989 * img[i, j, 0] + 0.5870 * img[i, j, 1] + 0.1140 * img[i, j, 2];
            YIQ[i, j, 1] = 0.596 * img[i, j, 0] - 0.274 * img[i, j, 1] - 0.322 * img[i, j, 2];
            YIQ[i, j, 2] = 0.211 * img[i, j, 0] - 0.523 * img[i, j, 1] + 0.312 * img[i, j, 2];
    return YIQ


def getCMY(img):
    # Load image with 32 bit floats as variable type
    bgr = np.float32(img) / 255

    # Separate color channels
    blue = bgr[:, :, 0]
    green = bgr[:, :, 1]
    red = bgr[:, :, 2]

    for i in range(0, blue.shape[0]):
        for j in range(0, blue.shape[1]):
            c = 1 - red
            m = 1 - green
            y = 1 - blue

    # Merge channels into picture and return image
    cmy = cv2.merge((c, m, y))
    return cmy


# read a coloured image
path="C:/Users/Danish/Desktop/DIVP/Images/icecream.jpg"
img = cv2.imread(path,cv2.IMREAD_COLOR)
# convert RGB to HSI
hsi = getHSI(img)
# convert RGB to YIQ
yiq = getYIQ(img)
# convert RGB to CMY
cmy = getCMY(img)

plt.figure(0)
plt.imshow(img)
plt.title('Original RGB image')

plt.figure(1)
plt.imshow(hsi)
plt.title('HSI image')

plt.figure(2)
plt.imshow(yiq)
plt.title('YIQ image')

plt.figure(3)
plt.imshow(cmy)
plt.title('CMY image')

plt.show()
