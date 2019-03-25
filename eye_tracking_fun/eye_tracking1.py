# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:49:42 2019

@author: TongDist
好像和2一样
模型： 
    dlib shape_predictor_68_face_landmarks
"""
import dlib

predictor_path='shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
#输入图像可以黑白，彩色
#返回先右眼 后左眼
def eye_tracking_1(img):
    dets = detector(img, 1)
    try:
        if dets[0]:
            for k, d in enumerate(dets):
                shape = predictor(img, d)
                x_total_left,y_total_left,x_total_right,y_total_right=0,0,0,0
                for point in range(36,42):
                    x_total_right+=shape.part(point).x
                    y_total_right+=shape.part(point).y
                    #print(shape.part(point))
                for point in range(42,48):
                    #print(shape.part(point))
                    x_total_left+=shape.part(point).x
                    y_total_left+=shape.part(point).y
                #print("===1===")
                return [[x_total_right/6,y_total_right/6],[x_total_left/6,y_total_left/6]]
        else:
            return -1
    except:
        return -1
