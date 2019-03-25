# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:04:12 2019

@author: TongDist
"""
import cv2
import numpy as np
# 图片识别方法封装
#返回 先右眼 后左眼
def eye_tracking_4(img):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes_center=[]
    cap = cv2.CascadeClassifier(
        #"D:\opencv\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml"
        #"D:\opencv\opencv\sources\data\haarcascades\haarcascade_lefteye_2splits.xml"
        #"D:\opencv\opencv\sources\data\haarcascades\haarcascade_righteye_2splits.xml"
        "haarcascade_eye_tree_eyeglasses.xml"
    )
    faceRects = cap.detectMultiScale(
        img, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50),maxSize=(90,90))
    try:
        if len(faceRects):
            #print("检测出"+str(len(faceRects))+"个目标！！")
            #print(np.sort(faceRects,axis=0))
            
            for faceRect in np.sort(faceRects,axis=0)[0:2]:
                x, y, w, h = faceRect
                eyes_center.append([x+h*0.5,y+w*0.5])
            return eyes_center
        else:
            return -1
    except:
        return -1
