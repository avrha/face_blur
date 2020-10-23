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

#get width and height
h, w = img.shape[:2]

#detect faces 
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(40,40),maxSize=(60,60))

for (x,y,w,h) in faces:
  cropped = img[y:y+h, x:w+w]
  cropped = cv2.GaussianBlur(cropped,(23,23),30)
  
  cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
  print(cropped.shape[0])
  l_img = img
  s_img = cropped
  y_offset = y
  x_offset = x
  l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
