# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:45:58 2019

@author: TongDist
"""

import compute_fun.get_circle_dir1 as gcd

print(gcd.init(size=40))

#print(gcd.load_all_circle_dir())

import cv2

img=cv2.imread('2.jpg',0)

all_circle_dir=gcd.load_all_circle_dir()

#print(gcd.get_max_index(dislist_temp))
'''
#         图片    所有圆心坐标         圆心 开始 结束 结果
def T_func(img_0,all_circle_dir_0,center_0,rr1,rr2,l_l):
    list_01=gcd.compute_circle_sum_list(img_0,all_circle_dir_0,center_0,rr1,rr2)
    dislist_12 = gcd.get_circle_dislist(list_01,1)
    #print(dislist_12)
    rrr=gcd.get_max_index(dislist_12)
    #print(rrr)
    l_l.append([center_0[0],center_0[1],rrr,max(dislist_12)])
'''
l=[]
import _thread as thread
import time
start=time.time()

import compute_fun.compute as com
for i in range(2,60):
    for j in range(2,30):
        #print(i,j)
        #iii((i,j),min(i,j,20),l)
        #thread.start_new_thread(gcd.T_func,(img,all_circle_dir,(i,j),1,min(i,j,20),l,1))
        #thread.start_new_thread(gcd.T_func,(img,all_circle_dir,(i,j+29),1,min(i,j+29,20),l,1))
        thread.start_new_thread(gcd.T_func,(img,all_circle_dir,(i,j),5,15,l,1))
        thread.start_new_thread(gcd.T_func,(img,all_circle_dir,(i,j+29),5,15,l,1))
#print(l)
'''
while(len(l)<58):
    print(len(l))'''
result=com.get_re(l)
print(result)
cv2.circle(img,(result[0],result[1]),result[2],(255,255,255),1)
'''
l_max=0
l_max2=[0,0,0]
for l1 in l:
    if l1[3]>l_max:
        l_max=l1[3]
        l_max2[0],l_max2[1],l_max2[2]=l1[0],l1[1],l1[2]
print(l_max)
print(l_max2)
'''
cv2.imshow('t',img)
print(time.time()-start)
cv2.waitKey(0)
cv2.destroyAllWindows()
