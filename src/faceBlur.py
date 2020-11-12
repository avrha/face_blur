import cv2
import dlib

#Load in and convert source image to into grayscale
img = cv2.imread('../pics/group2.jpg',1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces using CNN model
cnnFaceDetector = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat')
faces = cnnFaceDetector(gray,1)

#Blur faces
for faceRect in faces:
  rect = faceRect.rect
  x = rect.left()
  y = rect.top()
  w = rect.right() - x
  h = rect.bottom() - y

  box = img[y:y+h,x:x+w]
  box = cv2.GaussianBlur(box,(23,23),30)
  img[y:y+box.shape[0], x:x+box.shape[1]] = box 

#Display image with blur
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
