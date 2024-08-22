import cv2

img = cv2.imread('assets/my_pic.jpeg',1) #imread stands for image read. here 1 stands for it the image has some kind of transparency, it'll be displayed. 1 means coloured img without transparence and 0 means grey scale img. 

"""
cv2 by default loads an image in BLUE GREEN RED (BGR) pattern
"""

#img = cv2.resize(img, (200,200)) # resize the image to 200 by 200 pixels
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5 )	#resize the image by 0.5 times
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) #rotate it

cv2.imwrite('new_image.jpg', img)	#save the image. The first parameter is the photo title saved, and the second parameter is the image to be saved

cv2.imshow('Image', img)	#it opens the image after implementing the changes, and name of image is 'Image'
cv2.waitKey(0)				#the image will be open forever until the user presses the key 
cv2.destroyAllWindows()		#the opened image will be destroyed