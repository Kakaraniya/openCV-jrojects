import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
	ret, frame = cap.read()

	width = int(cap.get(3))#here 3 and 4 are properties for width and height. 
	height = int(cap.get(4))

	img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
	img = cv2.line(frame, (width,0), (0,height), (0,255,0), 5)
	img = cv2.rectangle(frame, (100,100), (200,200), (128,128,128), -1)
	img = cv2.circle(frame, (300,300),60, (0,0,255), 5)
	font = cv2.FONT_HERSHEY_SIMPLEX
	img = cv2.putText(img, 'I am great!', (200,height-30), font, 4, (0,0,0), 5, cv2.LINE_AA)


	cv2.imshow('frame', img)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

