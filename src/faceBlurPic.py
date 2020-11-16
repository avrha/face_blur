import cv2
from functions import faceBlur
import dlib

def main():
  #Load in and convert source image to into grayscale
  img = cv2.imread('../media/groupPic.jpg',1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  frameCount = 0
  faceCount = 0
  
  #Detect faces using CNN model
  cnnFaceDetector = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat')
  faces = cnnFaceDetector(gray,1)
  
  #Blur faces
  faceBlur(img,faces,frameCount,faceCount)

  #Display image with blur
  cv2.imshow("Image",img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  return 0

if __name__ == "__main__":
  main()
