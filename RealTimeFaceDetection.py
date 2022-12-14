import numpy as np
import cv2
from deepface import DeepFace
faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) 
cap.set(4,480) 
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result=DeepFace.analyze(img,actions=['emotion'], enforce_detection=False)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    font = cv2.FONT_HERSHEY_PLAIN

    cv2.putText(img,
    result['dominant_emotion'],
    (50,50),
    font,3,
    (255,0,0),
    2,
    cv2.LINE_4)

    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release()
cv2.destroyAllWindows()