#!/usr/bin/env python
# encoding: utf8

import cv2
import numpy as np
import gtk

def main():
    cam = cv2.VideoCapture(0)
    while True:
        img = cam.read()[1]
        blur = cv2.blur(img, (5, 5))
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,np.array((10,100,100)), np.array((30,255,255))) # yellow :)

        cv2.imshow("HSV", thresh)
        
        if cv2.waitKey(5) == 27:
            break

main()
