import numpy as np
import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)#here 1.3 is the scale factor. It is present to scale the size of the face to detect it. lower the value, more the acuracy but slower the processing
    # second factor is the minimum number of face detections
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5) #draw rect around face
        roi_gray = gray[y:y+w, x:x+w]# get the image of the face in gray scale. i.e. fetch all the pixels present inside rect
        roi_color = frame[y:y+h, x:x+w] #get the image in coloured scale
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.25, 5)#detect eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)#draw rect

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()