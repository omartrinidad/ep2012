import pyfits as pf
import numpy as np
import sys
import cv2

def fits2rgb(data):
    height, width = data.shape
    rgb = np.empty(shape=(height, width, 3), dtype=np.uint8)
    max = np.max(data)
    min = np.min(data)
    piece = 255.0/(max-min)
    for h in xrange(height):
        for w in xrange(width):
            channel = (data.item(w, h) - min)*piece
            rgb.itemset(w, h, 0, channel)
            rgb.itemset(w, h, 1, channel)
            rgb.itemset(w, h, 2, channel)
    return rgb

fitsfile = sys.argv[1]
data = pf.getdata(fitsfile)
height, width = data.shape

image_rgb = fits2rgb(data)

cv2.imshow("BGR image", image_rgb)
cv2.imshow("Original Image", data)
cv2.waitKey(10000)
