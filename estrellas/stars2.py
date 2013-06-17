import pyfits as pf
import numpy as np
import sys
import cv2

fitsfile = sys.argv[1]
data = pf.getdata(fitsfile)
height, width = data.shape

image = np.array(data, dtype = np.uint16)

gray = cv2.convertScaleAbs(image)

thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]
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

cv2.imshow("Row Image", image)
cv2.imshow("Thresh Image RGB", color)
cv2.waitKey(10000)
