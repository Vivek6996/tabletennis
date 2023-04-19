#Shi-Tomasi Corner Detection and Good Features to Track without Lines

import numpy as np
import cv2 
from matplotlib import pyplot as plt


img = cv2.imread('table2.jpeg')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corner detection
corners = cv2.goodFeaturesToTrack(gray, 21, 0.01, 10)
corners = np.int0(corners)

#drawing corners
for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

