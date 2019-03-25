# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:11:23 2019

@author: TongDist
为了方便获取 圆上坐标，直接全算出来，写成本地文件，用的时候读就行
"""

import cv2
import numpy as np

#获取矩阵中非零元素坐标
def get_nonzero(maxtrix):
    if isinstance(maxtrix,list):
        maxtrix = np.array(maxtrix) 
    x = maxtrix.nonzero()
    result=[]
    for i in range(len(x[0])):
        result.append([x[0][i],x[1][i]])
    return result
#获取圆上坐标      图片长  宽  圆心坐标  半径
def get_circle_dir(width,high,center,r):
    points=[]
    if isinstance(width,int) and isinstance(high,int) and isinstance(r,int):
        pass
    else:
        print('input wrong!\nneed int！')
    img_temp = np.zeros([width,high],np.uint8)
    cv2.circle(img_temp,center,r,(255,255,255),1)
#不知道为什么反而慢了
#    points=get_nonzero(img_temp)

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

import pickle
#初始化 写出circle坐标文件
def init(filename='./compute_fun/circle_model/pickle_circle_1.pkl',size=20):
    if not isinstance(size,int):
        print('input size is not int!!')
        return False
    try:
        with open(filename,'wb') as pickle_list:
            for i in range(1,size+1):
                pickle.dump(g_cir_list(i),pickle_list)
    except FileNotFoundError:
        #无法打开文件
        print("No such file or directory: ",filename)
        print('input filename is wrong!!')
    except:
        #未知错误
        print('somthing else wrong!!')
        
    return True

#读取存储在本地的circle 坐标
def load_all_circle_dir(filename='./compute_fun/circle_model/pickle_circle_1.pkl'):
    list_temp=[]
    try:
        with open(filename,'rb') as read_temp:
            i=0
            while(True):
                try:
                    list_temp.append(pickle.load(read_temp))
                    i+=1
                except EOFError:
                    #读到空，即读完
                    print("finish load!!")
                    list_temp.insert(0,i)
                    break
                
    except FileNotFoundError:
        #无法打开文件
        print("No such file or directory: ",filename)
        print('input filename is wrong!!')
    except:#未知错误
        print('somthing else wrong!!')
    #返回的列表 第一个元素是存的圆坐标的个数
    return list_temp
import random
#获取圆上坐标的和       图片  圆上点list  圆心
def compute_circle_sum(img,points,center,drop=0):
    sum_0=0
    if drop!=0 and drop<len(points):
        points=random.sample(points,drop)
    for point in points:
        sum_0+=img[point[0]+center[0]][point[1]+center[1]]
    return sum_0

#计算圆上坐标和的列表        图片 圆上点list 圆心 开始 结束
def compute_circle_sum_list(img,points,center,i,j,drop=0):
    list_temp=[]
    for i0 in range(i,j+1):
        list_temp.append(compute_circle_sum(img,points[i0],center,drop))
    return list_temp

#把sum列表变成dis列表
def get_circle_dislist(list_sum,flag=0):
    dislist=[]
    
    #flag=0  返回圆上像素和的差值
    if(flag==0):
        for i in range(0,len(list_sum)-1):
            dislist.append(list_sum[i+1]-list_sum[i])
        return dislist
    
    #其他，返回像素均值的差值
    else:
        for i in range(0,len(list_sum)-1):
            dislist.append(list_sum[i+1]/(i+2)-list_sum[i]/(i+1))
        return dislist

#返回列表中最大元素的索引
def get_max_index(dislist_0):
    return dislist_0.index(max(dislist_0))+2

#           图片   所有圆上坐标     圆心坐标 开始结束 结果 0和 1均值
def T_func(img_0,all_circle_dir_0,center_0,rr1,rr2,l_l,flag=0,drop=0):
    #获取圆心上  各半径圆上像素和  的列表
    list_01=compute_circle_sum_list(img_0,all_circle_dir_0,center_0,rr1,rr2,drop)
    #获取  其差值列表
    dislist_12 = get_circle_dislist(list_01,flag)
    #dislist_12 = gcd.get_circle_dislist(list_01,1)
    #print(dislist_12)
    rrr=get_max_index(dislist_12)
    #print(rrr)
    
    #取最大时      圆心坐标               半径     最大的差
    l_l.append([center_0[0],center_0[1],rrr+rr1,max(dislist_12)])

if __name__=='__main__':
    pass