import cv2

img = cv2.imread('images/img1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB Image', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()