#TODO 
#Argument support
#Modularize code 

import cv2
import dlib
from imutils import face_utils

cap = cv2.VideoCapture('../media/groupVid.mp4')
cnnFaceDetector = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat')

if(cap.isOpened() == 0):
  print("Error opening the video file")

while(cap.isOpened()):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.resize(gray,(0,0),fx=0.25,fy=0.25)
  
  if ret == 1:
      #skip frame
      if cap.get(1) % 5 == 0:
        faces = cnnFaceDetector(gray,1)
        frameCount = cap.get(1)
        faceCount = 0

        for faceRect in faces:
          #retrieve dimensions on detected face
          rect = faceRect.rect
          x = rect.left()
          y = rect.top()
          w = rect.right() - x
          h = rect.bottom() - y
          
          #create object based on retrieved dimensions
          box = frame[y:y+h,x:x+w]
          box = cv2.GaussianBlur(box,(23,23),30)
          #overlay object on frame
          frame[y:y+box.shape[0], x:x+box.shape[1]] = box 
          faceCount += 1

          if faceCount == len(faces):
            print("Frame:",frameCount,"Face:",faceCount) 
            cv2.imshow('Video',frame)
            print("----------------------")

          else:
            print("Frame:",frameCount,"Face:",faceCount) 
            cv2.imshow('Video',frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
          break

  else:
    break

cap.release()
cv2.destroyAllWindows()
