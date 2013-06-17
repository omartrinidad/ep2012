#!/usr/bin/env python
# encoding: utf8

import cv2
import numpy as np

def main():
    cam = cv2.VideoCapture(0)
    x = 0
    y = 0
    img = cam.read()[1]
    tracking = np.zeros(shape=(img.shape[0],img.shape[1]))
    while True:
        img = cam.read()[1]
        tracking2 = np.zeros(shape=(img.shape[0],img.shape[1]))
        blur = cv2.blur(img, (5, 5))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,np.array((10,100,100)), np.array((30,255,255))) # yellow :)
        # thresh = cv2.inRange(hsv,np.array((0,0,0)), np.array((30,30,30))) # black :)

        cv2.imshow("HSV", thresh)
        cv2.imshow("Blur", blur)
        
        moments = cv2.moments(thresh)
        area = moments['m00']
        xx = x
        yy = y
        try:
            x = int(moments['m10']/area)
            y = int(moments['m01']/area)
        except:
            print "area = 0"
        cv2.circle(tracking2, (x, y), 30, (255,255,255), thickness = 4)
        if xx>0 and yy>0 and x>0 and y>0:
            cv2.line(tracking, (x,y), (xx, yy), (255), thickness = 15)
            cv2.imshow("Tracking", tracking)
            cv2.imshow("Tracking2", tracking2)
        
        if cv2.waitKey(5) == 27:
            break

main()
