#!/usr/bin/env python
# encoding: utf8

import cv2
import numpy as np

def main():
    cam = cv2.VideoCapture(0)
    while True:
        img = cam.read()[1]
        blur = cv2.blur(img, (7, 7))
        cv2.imshow("Image blurred", blur)
        cv2.imshow("Image", img)
        
        if cv2.waitKey(5) == 27:
            break

main()
