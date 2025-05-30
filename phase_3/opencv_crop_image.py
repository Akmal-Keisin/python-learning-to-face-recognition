import cv2
import numpy as np

img = cv2.imread('images/img1.jpg')
cropped = img[100:400, 100:400]  # Crop the image from (100, 100) to (400, 400)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()