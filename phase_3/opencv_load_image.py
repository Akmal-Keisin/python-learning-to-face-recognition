import cv2
import numpy as np

img = cv2.imread('images/img1.jpg')
print(type(img))
print(img.shape)
print(img[0, 0])
print(img.dtype)
print(img.size)
