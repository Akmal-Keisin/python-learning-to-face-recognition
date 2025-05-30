import cv2

img = cv2.imread('images/img1.jpg')
cv2.rectangle(img, (100, 100), (300, 300), (0, 255, 0), thickness=2)
cv2.circle(img, (250, 250), 40, (255, 0, 0), -1)
cv2.putText(img, "Hello", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('Image with Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()