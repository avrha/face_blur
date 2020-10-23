import numpy as np
import cv2

#set paths
img_path = '/home/avrha/Desktop/faceBlur/pics/group1.jpg'
xml_path = '/home/avrha/Desktop/faceBlur/pics/haarcascade_frontalface_default.xml'

#read in image
img = cv2.imread(img_path,1)

#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create cascade object
face_cascade =  cv2.CascadeClassifier(xml_path)

#detect faces 
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(40,40),maxSize=(60,60))

#draw faces on the source image
for (x,y,w,h) in faces:
  cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

#output image
cv2.imshow("faces",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
