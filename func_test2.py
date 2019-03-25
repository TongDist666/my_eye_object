# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:46:39 2019

@author: TongDist

"""

from eye_tracking_fun.eye_tracking1 import eye_tracking_1
#from eye_tracking_fun.eye_tracking2 import eye_tracking_2
#from eye_tracking_fun.eye_tracking3 import eye_tracking_3
#from eye_tracking_fun.eye_tracking4 import eye_tracking_4
import cv2
import time
from eye_tracking_fun.simple_function import getEyeArea 
    
cap = cv2.VideoCapture(0)
eye_tracking_1_dir_center_point_obj=[]
import compute_fun.get_circle_dir1 as gcd

#初始化
print(gcd.init(size=40))
#获取所有圆 上 坐标的相对坐标
all_circle_dir=gcd.load_all_circle_dir()
import compute_fun.compute as com
import _thread as thread
while cv2.waitKey(1)!=27:
    start = time.time()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    print("---1---")
    eye_points=eye_tracking_1(gray)
    try:
        x_1=int(eye_points[0][0])
        y_1=int(eye_points[0][1])
        x_2=int(eye_points[1][0])
        y_2=int(eye_points[1][1])
    except:
        continue

    test=getEyeArea(gray,[x_1,y_1],80)
    edges=cv2.Canny(test,100,200)
    test_sobel=cv2.Sobel(test,cv2.CV_64F,1,0,ksize=5)
    l=[]
    for i in range(40-5,40+5):
        for j in range(40-5,40+5):
            
            thread.start_new_thread(gcd.T_func,(edges,all_circle_dir,(i,j),5,15,l,1))
            #thread.start_new_thread(gcd.T_func,(edges,all_circle_dir,(i,j),5,min(10,i,j),l,1))
        
    result=com.get_re(l)
    print(result)
    rimg=cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    cv2.circle(rimg,(result[0],result[1]),result[2],(0,0,255),1)
    #cv2.imshow('test',test)
    
    
    cv2.imshow("test",rimg)
    
    #b,g,r=cv2.split(test_rgb)
    #cv2.imshow("b",b)
    #cv2.imshow("g",g)
    #cv2.imshow("r",r)
    #print(test_rgb)
    #print(test)
    
    
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