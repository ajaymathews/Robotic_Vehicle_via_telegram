#import RPi.GPIO as GPIO
import numpy as np
import cv2
import serial
import time

'''GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35,0)


GPIO.output(35,1)'''

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')


cap = cv2.VideoCapture(0)

fire_flag=0

while 1:
    try:
        ret, img = cap.read()
        cv2.imshow('imgorignal',img) #
        fire = fire_cascade.detectMultiScale(img, 1.2, 5)
        for (x,y,w,h) in fire:
            fire_flag=fire_flag+1
##            print 'Inside'
            
        if(fire_flag>1):
            '''GPIO.output(35,0)'''
            print('Fire is detected..!')
            fire_flag=0
            '''GPIO.output(35,1)'''

        cv2.waitKey(30)
    except:
        pass
        

