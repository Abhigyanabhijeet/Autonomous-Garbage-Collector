import cv2
import cv2.aruco as aruco
import math
import bluetooth
import sys
import serial
import numpy as np

#import detecting_corners as angle

#Blutooth Connection


 


def lval(flag):
    l=0
    
    if flag==0:
        l=2
    else:
        l=1

    return l




cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    #print(corners)
    gray = aruco.drawDetectedMarkers(frame, corners)
    count=1;
 
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    if corners:
        centerX=int((corners[0][0][0][0]+corners[0][0][2][0])//2)
        centerY=int((corners[0][0][0][1]+corners[0][0][2][1])//2)
        cv2.putText(frame,'o',(centerX,centerY),font,1,(0,0,255),2,cv2.LINE_AA)
        posX=int((corners[0][0][0][0]+corners[0][0][1][0])//2)
        posY=int((corners[0][0][0][1]+corners[0][0][1][1])//2)
        #cv2.putText(frame,'North',(posX,posY),font,1,(255,255,255),1,cv2.LINE_AA)
        cv2.circle(frame,(posX,posY),10,(0,0,255),-1)
        
        verX=centerX
        verY=0
        a=math.sqrt(math.pow((verX - centerX),2) + math.pow((verY - centerY),2))
        b=math.sqrt(math.pow((centerX - posX),2) + math.pow((centerY - posY),2))
        c=math.sqrt(math.pow((verX - posX),2) + math.pow((verY - posY),2))
        angle = int(math.acos((math.pow(a,2)+math.pow(b,2)-math.pow(c,2))/(2*a*b))*180/math.pi)
        if(posX<centerX):
            angle=360-angle
        
            
        cv2.putText(frame,str(angle),(centerX,centerY),font,1,(255,0,0),2,cv2.LINE_AA)        
    
        
        
        
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
cap.release()
cv2.destroyAllWindows()
    

