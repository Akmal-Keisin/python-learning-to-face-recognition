import cv2
import numpy as np

# Show an image using OpenCV
img = cv2.imread('images/img1.jpg')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
