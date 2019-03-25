# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:41:57 2019

@author: TongDist
face_landmarks  model="small"
"""

import face_recognition

def eye_tracking_3(img):
    face_landmarks_list = face_recognition.face_landmarks(img,model="small")
    try:
        if face_landmarks_list[0]:
            left=face_landmarks_list[0]['left_eye']
            right=face_landmarks_list[0]['right_eye']
            
            #先右眼 后左眼
            return [[(left[0][0]+left[1][0])/2,(left[0][1]+left[1][1])/2],
                    [(right[0][0]+right[1][0])/2,(right[0][1]+right[1][1])/2]
                    ]
    except:
        return -1
