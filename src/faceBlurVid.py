#Todo
#Argument support
#Modularize code 

import cv2
import dlib
from imutils import face_utils
from functions import faceBlur

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

      faceBlur(frame,faces,frameCount,faceCount)

    if cv2.waitKey(25) & 0xFF == ord('q'):
       break
  else:
    break

cap.release()
cv2.destroyAllWindows()
