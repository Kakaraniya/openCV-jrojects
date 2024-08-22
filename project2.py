import cv2
import random

img = cv2.imread('assets/my_pic.jpeg', -1)

# Change first 100 rows to random pixels
for i in range(150):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]


print(img.shape)

#Copy part of image
tag = img[100:350, 200:450]
img[300:550, 100:350] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()