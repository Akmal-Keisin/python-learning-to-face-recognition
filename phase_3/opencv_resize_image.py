import cv2
import numpy as np

# Resize an image using OpenCV
img = cv2.imread('images/img1.jpg')
resizedimg = cv2.resize(img, (int(img.shape[1] * 2), int(img.shape[0] * 2)))

# # Save an image using OpenCV
cv2.imwrite('stored_images/resized_img1.jpg', resizedimg)