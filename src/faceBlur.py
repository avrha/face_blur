import numpy as np
import cv2

img_path = '/home/avrha/Desktop/faceBlur/pics/group1.jpg'
xml_path = '/home/avrha/Desktop/faceBlur/xml/haarcascade_frontalface_default.xml'

img = cv2.imread(img_path,1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade =  cv2.CascadeClassifier(xml_path)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(40,40),maxSize=(60,60))

for (x,y,w,h) in faces:
  
  cropped = img[y:y+h, x:x+w]
  cropped = cv2.GaussianBlur(cropped,(23,23),30)
  
  img[y:y+cropped.shape[0], x:x+cropped.shape[1]] = cropped 

cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
