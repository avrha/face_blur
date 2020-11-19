import cv2
import dlib
import argparse
import numpy as np
from blur_filter import blur_cnn


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to image file")
args = vars(ap.parse_args())


def main():
  # Load in and convert source image to into grayscale
  img = cv2.imread(args["input"],1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.resize(gray,(0,0),fx=0.25,fy=0.25)

  if np.shape(img) == ():
    print("Error opening the image file")
    exit()

  #Detect faces using CNN model
  face_detect = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat') 
  face = face_detect(gray,1)

  #Blur faces
  blur_cnn(img,face)

  #Display image with blur
  cv2.imshow("Output",img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
