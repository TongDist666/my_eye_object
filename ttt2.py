# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:47:49 2019
 
@author: TongDist
"""
import cv2
import numpy as np

def hough_test(img):
    edges=cv2.Canny(img,180,210)
    edge=cv2.cvtColor(edges,cv2.COLOR_GRAY2RGB)
    try:
        #circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,
        #param1=50,param2=30,minRadius=min_v,maxRadius=max_v)
        circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,10,
        param1=41,param2=18,minRadius=5,maxRadius=20)
    
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(edge,(i[0],i[1]),i[2],(0,255,0),2)
            print(i[2])
            # draw the center of the circle
            cv2.circle(edge,(i[0],i[1]),2,(0,0,255),3)
    except:
        print('something wrong')
    return edge
if __name__=='__main__':
    im=cv2.imread('2.jpg',0)
    imm=hough_test(im)
    cv2.imshow('test',imm)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
