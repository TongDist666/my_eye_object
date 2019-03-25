# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:19:38 2019

@author: TongDist 
face_recognition   
"""

import face_recognition
#输入图像可以黑白，彩色
def eye_tracking_2(frame):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_landmarks_list = face_recognition.face_landmarks(frame)
    left_x,right_x,left_y,right_y=0,0,0,0
    try:
        if face_landmarks_list[0]['left_eye']:
            for left_point in face_landmarks_list[0]['left_eye']:
                #print(left_point)  右眼
                left_x+=left_point[0]
                left_y+=left_point[1]
        if face_landmarks_list[0]['right_eye']:
            for right_point in face_landmarks_list[0]['right_eye']:
                #print(right_point)  左眼
                right_x+=right_point[0]
                right_y+=right_point[1]
        #print('===2===')
        return [[left_x/6,left_y/6],[right_x/6,right_y/6]]
    except:
        return -1
