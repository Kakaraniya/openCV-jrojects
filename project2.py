import cv2
import random

img = cv2.imread('assets/my_pic.jpg', -1)

# Change first 100 rows to random pixels
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

print(img.shape)

#Copy part of image
tag = img[100:200, 300:400]
img[300:400, 100:200] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()