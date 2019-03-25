# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:00:22 2019

@author: dell
"""

from eye_tracking_fun.eye_tracking1 import eye_tracking_1
#from eye_tracking_fun.eye_tracking2 import eye_tracking_2
#from eye_tracking_fun.eye_tracking3 import eye_tracking_3
#from eye_tracking_fun.eye_tracking4 import eye_tracking_4
import cv2
import numpy as np
from eye_tracking_fun.simple_function import getEyeArea 

def nothing(x):
    pass


eye_tracking_1_dir_center_point_obj=[]
cv2.namedWindow('canny',1)
cv2.namedWindow('res',2)
#min 211 max 180 minRadius 0 maxRadius 30 param1 41 param2 18
cv2.createTrackbar('min','res',0,255,nothing)
cv2.createTrackbar('max','res',0,255,nothing)

cv2.createTrackbar('minRadius','res',0,30,nothing)
cv2.createTrackbar('maxRadius','res',30,100,nothing)
cv2.createTrackbar('param1','res',10,50,nothing)
cv2.createTrackbar('param2','res',4,30,nothing)

img=cv2.imread('1.jpg',0)

while cv2.waitKey(1)!=27:
    print("---  ---")
    eye_points=eye_tracking_1(img)
    x_1=int(eye_points[0][0])
    y_1=int(eye_points[0][1])
    x_2=int(eye_points[1][0])
    y_2=int(eye_points[1][1])

    test=getEyeArea(img,[x_1,y_1],80)
    #cv2.imwrite('2.jpg',test)
    
    maxVal=cv2.getTrackbarPos('max','res')
    minVal=cv2.getTrackbarPos('min','res')
    min_v = cv2.getTrackbarPos('minRadius','res')
    max_v = cv2.getTrackbarPos('maxRadius','res')
    
    p1 = cv2.getTrackbarPos('param1','res')
    p2 = cv2.getTrackbarPos('param2','res')
    
    edges=cv2.Canny(test,minVal,maxVal)
    edge=cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
    #
    try:
        #circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,
        #param1=50,param2=30,minRadius=min_v,maxRadius=max_v)
        circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,
        param1=p1,param2=p2,minRadius=min_v,maxRadius=max_v)
    
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(edge,(i[0],i[1]),i[2],(0,255,0),2)
            print(i[2])
            # draw the center of the circle
            cv2.circle(edge,(i[0],i[1]),2,(0,0,255),3)
    except:
        print('something wrong')
    
    #b,g,r=cv2.split(test_rgb)
    #cv2.imshow("b",b)
    #cv2.imshow("g",g)
    #cv2.imshow("r",r)
    #print(test_rgb)
    #print(test)
    cv2.imshow("canny",edge)
    
cv2.destroyAllWindows()