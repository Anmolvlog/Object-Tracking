import cv2
import numpy as np

cap=cv2.VideoCapture(0)



while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #red color
    lowerLimit=np.array([0,100,100])
    upperLimit=np.array([20,255,255])
    
    mask=cv2.inRange(hsv,lowerLimit,upperLimit)
    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',result)
    
    if(cv2.waitKey(1)& 0xFF == ord('q')):
        break
        
        
destroyAllWindows()
    
    