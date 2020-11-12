import cv2
import dlib
from imutils import face_utils

cap = cv2.VideoCapture('../media/groupVid.mp4')

if(cap.isOpened() == 0):
  print("Error opening the video file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == 1:
    cnnFaceDetector = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat')
    faces = cnnFaceDetector(gray,1)

    for faceRect in faces:
      rect = faceRect.rect
      x = rect.left()
      y = rect.top()
      w = rect.right() - x
      h = rect.bottom() - y

      box = frame[y:y+h,x:x+w]
      box = cv2.GaussianBlur(box,(23,23),30)
      frame[y:y+box.shape[0], x:x+box.shape[1]] = box 

      cv2.imshow('Video',frame)
      print(box)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
