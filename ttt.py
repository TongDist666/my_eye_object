# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:28:09 2019
 
@author: TongDist
"""

import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_path = 'i.jpg'
img = cv2.imread(img_path,0)
gray = img
# cv2.imshow('original_img', img)
# cv2.imshow('gray', gray)
# cv2.waitKey()

#对模糊图像二值化。梯度图像中不大于90的任何像素都设置为0（黑色）。 否则，像素设置为255（白色）
(_, thresh) = cv2.threshold(gray, 53, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('thresh', thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel,None,(-1,-1),1)
# cv2.imshow('closed', closed)
# cv2.waitKey(0)#无限期等待输入

(_, cnts, _) = cv2.findContours(closed,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# draw a bounding box arounded the detected barcode and display the image
img_copy = img.copy()
cv2.drawContours(img_copy, cnts, -1, (0, 255, 0), 1)
