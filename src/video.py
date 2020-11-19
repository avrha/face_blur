import cvlib as cv
import numpy as np
import cv2
import argparse
from blur_filter import blur_dnn 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to video file")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["input"])

if not cap.isOpened():
  print("Could not open file")
  exit()


while cap.isOpened():
  ret, frame = cap.read()

  if not ret:
    print("Error with ret")
    exit()
  
  if np.shape(frame) == ():
    print("Error with frame")
    exit()

  face, _ = cv.detect_face(frame)
  blur_dnn(frame,face)
  cv2.imshow("Real-time face detection", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
