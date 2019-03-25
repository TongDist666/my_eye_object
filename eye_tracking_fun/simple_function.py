# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:28:36 2019

@author: TongDist
"""
import cv2
#重置数组，返回数组长度
def release_dir(dir_list):
    dir_list=[]
    return len(dir_list)
def getEyeArea(img,center_point,size):
    return img[int(center_point[1]-size/2):int(center_point[1]+size/2),
               int(center_point[0]-size/2):int(center_point[0]+size/2)]
def is_point(point):
    return len(point)==2

#输入双眼中心坐标  和要返回矩形的边长
def pointsToRectangleArea(points,size):
    points_len=len(points)
    #输入点只有一个
    if points_len==1:
        print("仅检测出一个点!")
        if size%2==0 and size>2:
            if is_point(points[0]):
                #矩形左上角点坐标
                #[point[0]-size*0.5,point[1]-size*0.5]
                #矩形右下角点坐标
                #[point[0]+size*0.5,point[1]+size*0.5]
                return [[points[0][0]-size*0.5,points[0][1]-size*0.5],[points[0][0]+size*0.5,points[0][1]+size*0.5]]
            else:
                #print("point数据格式不对！！")
                return -1
        else:
            #print("size 太小或非偶数，请重新选择！")
            return 0
    #两个输入点
    elif points_len==2:
        if size%2==0 and size>2:
            print("检测出两个点!")
            #Rectangle_area=[]
            if is_point(points[0]) and is_point(points[1]):
                #矩形左上角点坐标
                #Rectangle_area.append([point[0]-size*0.5,point[1]-size*0.5])
                #矩形右下角点坐标
                #Rectangle_area.append([point[0]+size*0.5,point[1]+size*0.5])
                return [
                        [points[0][0]-size*0.5,points[0][1]-size*0.5],
                        [points[0][0]+size*0.5,points[0][1]+size*0.5],
                        [points[1][0]-size*0.5,points[1][1]-size*0.5],
                        [points[1][0]+size*0.5,points[1][1]+size*0.5]]
            else:
                #print("point数据格式不对！！")
                return -1
        else:
            #print("size 太小或非偶数，请重新选择！")
            return 0
    #其他
    else:
        #print("输入points为空或超过2个！！！")
        return 1

'''
a=[[1,2],[3,4]]
b=[(1,2),(3,4)]

print(pointsToRectangleArea([[1,3,2]],4))
import random
import time
start=time.time()
for i in range(0,10):
    print(pointsToRectangleArea(
            [[random.randint(1,10),random.randint(1,10)],
              [random.randint(1,10),random.randint(1,10)]],4))
print(time.time()-start)
'''