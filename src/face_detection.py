import cv2
import dlib
import argparse
import numpy as np
import cvlib as cv
from src.blur_filter import blur_cnn, blur_dnn

def image(arg1,arg2):
  # Load in and convert source image to into grayscale
  img = cv2.imread(arg1,1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.resize(gray,(0,0),fx=0.25,fy=0.25)

  if np.shape(img) == ():
    print("Error opening the image file")
    exit()
  #Detect faces using CNN model

  face_detect = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat') 
  face = face_detect(gray,1)

  #Blur faces
  blur_cnn(img,face)

  #Display image with blur
  cv2.imshow("Output",img)
  cv2.imwrite(arg2,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


def video(arg1,arg2):
  ap = argparse.ArgumentParser()
  ap.add_argument("-i", "--input", required=True, help="Path to video file")
  ap.add_argument("-o", "--output", required=True, help="Name of output file")
  args = vars(ap.parse_args())

  cap = cv2.VideoCapture(arg1)

  if not cap.isOpened():
    print("Could not open file")
    exit()


  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))
  out = cv2.VideoWriter(arg2,cv2.VideoWriter_fourcc('M','J','P','G'),24,(frame_width,frame_height))

  while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
      print("Error with ret")
      exit()
    
    if np.shape(frame) == ():
      print("Error with frame")
      exit()
    
    # Load DNN model and then detect face
    face, _ = cv.detect_face(frame)
    blur_dnn(frame,face)
    out.write(frame)
    cv2.imshow("Real-time face detection", frame)

    # Press q to exit video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
