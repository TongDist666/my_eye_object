# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:03:37 2019
 
@author: TongDist
手点标记
"""

import cv2

cap = cv2.VideoCapture(0)

x1,y1,x2,y2,flag1=0,0,0,0,0

def label(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global flag1
        if flag1==0:
            global x1,y1
            x1,y1=x,y
            flag1=1
            print('11')
        elif flag1==1:
            global x2,y2
            x2,y2=x,y
            flag1=2
            print('22')
            
cv2.namedWindow('image')
cv2.setMouseCallback('image',label)
while(cv2.waitKey(1)!=27):
    ret,img=cap.read()
    
    if flag1==1:
        #print('1')
        continue
    elif flag1==2:
        print(x1,y1,' ',x2,y2)
        cv2.imwrite('./simple_label/'+str(x1)+'_'+str(y1)+'.jpg',img)
        x1,y1,x2,y2,flag1=0,0,0,0,0
    cv2.imshow('image',img)
cv2.destroyAllWindows()
