# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:44:07 2019

@author: TongDist
"""

#获取  圆上像素和 差值最大的 [x,y,半径,差值]
def get_re(l):
    l_max=[0,0,0,0]
    for l1 in l:
        if l1[3]>l_max[3]:
            l_max=l1
    return l_max
