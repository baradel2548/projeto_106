import cv2
import time
import math
import numpy as np

cap = cv2.VideoCapture("C:/Users/barad/Downloads/python/PRO_1-1_C106_TemplateProjeto-main/walking.avi")
body_cascade = cv2.CascadeClassifier('C:/Users/barad/Downloads/python/PRO_1-1_C106_TemplateProjeto-main/haarcascade_fullbody.xml')

while True:
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray,1.2,3)
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('pedestres',frame)
    if cv2.waitKey(1)==32:
        break
cap.release()
cv2.destroyALLwindows()