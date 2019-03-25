# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:04:29 2019

@author: TongDist
"""

import cv2
import numpy as np

#获取圆上坐标      图片长  宽  圆心坐标  半径
def get_circle_dir(width,high,center,r):
    points=[]
    img_temp = np.zeros([width,high],np.uint8)
    cv2.circle(img_temp,center,r,(255,255,255),1)
    for x in range(0,width):
        for y in range(0,high):
            if img_temp[x][y]!=0:
                points.append([x,y])
    '''      
    cv2.imshow('test',img_temp)
    print(img_temp)
    '''
    return points

#获取标准化 的 圆上坐标
def g_cir_list(i):
    i_list=get_circle_dir(2*(i+1),2*(i+1),(i+1,i+1),i)
    for i_l in i_list:
        i_l[0]-=(i+1)
        i_l[1]-=(i+1)
    return i_list


print(g_cir_list(1))
print(g_cir_list(2))
print(g_cir_list(3))
print('- - - -')
import pickle
#写
pickle_list = open('pickle_circle.pkl','wb')

pickle.dump(g_cir_list(1),pickle_list)
pickle.dump(g_cir_list(2),pickle_list)
pickle.dump(g_cir_list(3),pickle_list)
pickle.dump(g_cir_list(4),pickle_list)
pickle.dump(g_cir_list(5),pickle_list)
pickle.dump(g_cir_list(6),pickle_list)
pickle.dump(g_cir_list(7),pickle_list)
pickle.dump(g_cir_list(8),pickle_list)
pickle.dump(g_cir_list(9),pickle_list)
pickle.dump(g_cir_list(10),pickle_list)
pickle.dump(g_cir_list(11),pickle_list)
pickle.dump(g_cir_list(12),pickle_list)
pickle_list.close()

#读
read_test=open('pickle_circle.pkl','rb')
while(True):
    try:
        print(pickle.load(read_test))
    except:
        print("that's all")
        break

read_test.close()

print('---')
p1=get_circle_dir(4,4,(2,2),1)
print(p1)
for p in p1:
    p[0]-=2
    p[1]-=2
print(p1)

p2=get_circle_dir(6,6,(3,3),2)
print(p2)
for p in p2:
    p[0]-=3
    p[1]-=3
print(p2)

print('---')
#圆上像素和     图像  点坐标
def circle_sum(img,points):
    sum0=0
    for point in points:
        sum0+=img[point[0],point[1]]
    return sum0

def start_try(img_0,start_point,start_r):
    sum_list=[]
    for i in range(start_r,20):
        points_temp = get_circle_dir(80,80,start_point,i)
        sun_temp = circle_sum(img_0,points_temp)
        sum_list.append(sun_temp)
    return sum_list

img2=cv2.imread('2.jpg',0)
#cv2.circle(img2,(40,40),5,(255,255,255),1)

cv2.imshow('2',img2)
import time
start = time.time()
points2=get_circle_dir(80,80,(40,40),5)
print(time.time()-start)
start = time.time()
print(circle_sum(img2,points2))
print(time.time()-start)
start = time.time()
su=start_try(img2,(40,40),1)
print(time.time()-start)
d=[]
for s in range(0,len(su)-1):
   d.append(su[s+1]-su[s]) 
print(su)
print(d)

cv2.circle(img2,(40,40),8,(255,255,255),1)
cv2.imshow('3',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()