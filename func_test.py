# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:55:01 2019

@author: TongDist

"""

from eye_tracking_fun.eye_tracking1 import eye_tracking_1
#from eye_tracking_fun.eye_tracking2 import eye_tracking_2
#from eye_tracking_fun.eye_tracking3 import eye_tracking_3
#from eye_tracking_fun.eye_tracking4 import eye_tracking_4
import cv2
import time
import numpy as np                                            
from eye_tracking_fun.simple_function import getEyeArea 
    
cap = cv2.VideoCapture(0)
eye_tracking_1_dir_center_point_obj=[]

while cv2.waitKey(1)!=27:
    start = time.time()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    print("---1---")
    eye_points=eye_tracking_1(gray)
    try:
        #右眼
        x_1=int(eye_points[0][0])
        y_1=int(eye_points[0][1])
        #左眼
        x_2=int(eye_points[1][0])
        y_2=int(eye_points[1][1])
    except:
        continue

    right=getEyeArea(gray,[x_1,y_1],80)
    left=getEyeArea(gray,[x_2,y_2],80)
    right_edges=cv2.Canny(right,100,200)
    
    #拼成一个图片
    tempimg=np.hstack((left,right))
    #test_sobel=cv2.Sobel(right,cv2.CV_64F,1,0,ksize=5)
    #b,g,r=cv2.split(test_rgb)
    #cv2.imshow("b",b)
    #cv2.imshow("g",g)
    #cv2.imshow("r",r)
    #print(test_rgb)
    #print(test)
    cv2.imshow('t',tempimg)
    #cv2.imshow("left",left)
    #cv2.imshow("right",right)
    
    for eye in eye_points:
        cv2.circle(gray,(int(eye[0]),int(eye[1])),6,(0,0,255),3)
    
    #cv2.imshow("you",frame[y_1-30:y_1+30,x_1-30:x_1+30])
    #cv2.imshow("zuo",frame[y_2-30:y_2+30,x_2-30:x_2+30])
    #cv2.imshow("gray",gray)
    
    #cv2.imshow("123",eye)
    #print("---2---")
    #print(eye_tracking_2(gray))
    #print("---3---")
    #print(eye_tracking_3(gray))
    #print("---4---")
    #print(eye_tracking_4(gray))
    
    print("FPS："+str(1/(time.time()-start)))

cap.release()
cv2.destroyAllWindows()