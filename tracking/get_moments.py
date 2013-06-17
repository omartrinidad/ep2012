#!usr/bin/env python
# encoding: utf8

import cv2
import numpy as np

def main():
    cam = cv2.VideoCapture(0)
    while True:
        img = cam.read()[1]
        tracking2 = np.zeros(shape=(img.shape[0],img.shape[1]))
        blur = cv2.blur(img, (7, 7))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,np.array((10,100,100)), np.array((30,255,255))) # yellow :)
        
        moments = cv2.moments(thresh)
        cv2.imshow("Thresh", thresh)
        area = moments['m00']
        
        try:
            x = int(moments['m10']/area)
            y = int(moments['m01']/area)
        except:
            print "area = 0"
        
        if cv2.waitKey(5) == 27:
            break

main()
