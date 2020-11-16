import cv2
from imutils import face_utils

def faceBlur(frame,faces,frameCount,faceCount):
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
