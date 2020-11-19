import cv2
import dlib
import argparse
import numpy as np
import sys
from src.blur_filter import blur_cnn
import os

path = os.getcwd()

def image(arg1,arg2):
  # Load in and convert source image to into grayscale
  img = cv2.imread(arg1,1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.resize(gray,(0,0),fx=0.25,fy=0.25)

  if np.shape(img) == ():
    print("Error opening the image file")
    exit()
  #Detect faces using CNN model

  face_detect = dlib.cnn_face_detection_model_v1('../../model/mmod_human_face_detector.dat') 
  face = face_detect(gray,1)

  #Blur faces
  blur_cnn(img,face)

  #Display image with blur
  cv2.imshow("Output",img)
  cv2.imwrite(arg2,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
