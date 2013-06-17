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

image = np.empty(shape=(height, width, 1), dtype = np.uint16)

for x in xrange(height):
    for y in xrange(width):
        image.itemset(x, y, 0, data.item(x,y))

gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 5, 255, cv2.THRESH_BINARY_INV)[1]

color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
mask = np.zeros((height + 2, width + 2), np.uint8)

squares = []
for h in xrange(height):
    for w in xrange(width):
        if thresh[h, w] == 0:
            a = cv2.floodFill(color, mask, (w, h), (255, 0, 0))
            squares.append(a[1])

for coord in squares:
    x, y, w, h = coord
    cv2.rectangle(color, (x, y), (x+w , y+h), (0,0,255), thickness = 1, lineType=8)

cv2.imshow("Regtangles", color)
cv2.waitKey(10000)
