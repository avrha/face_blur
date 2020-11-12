import cv2
import dlib
from imutils import face_utils

cap = cv2.VideoCapture('../media/groupVid.mp4')
face_detect = dlib.get_frontal_face_detector()

if(cap.isOpened() == 0):
  print("Error opening the video file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == 1:
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = face_detect(gray,1)

    for (i,rects) in enumerate(rects):
      (x,y,w,h) = face_utils.rect_to_bb(rects)
      box = frame[y:y+h,x:x+w]
      box = cv2.GaussianBlur(box,(23,23,),30)
      frame[y:y+box.shape[0],x:x+box.shape[1]] = box

      cv2.imshow('Video',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else:
    break

cap.release()
cv2.destroyAllWindows()
