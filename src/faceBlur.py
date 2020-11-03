import cv2
import matplotlib.pyplot as plt
import dlib
import numpy as np
from imutils import face_utils
import matplotlib.image as mpimg
font = cv2.FONT_HERSHEY_SIMPLEX

img_path = '/home/avrha/Desktop/faceBlur/pics/group1.jpg'

source = mpimg.imread(img_path)
blurred = source.copy()

gray =  cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
img = np.float32(gray) / 32

#Calculate gradient
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)
mag, angle = cv2.cartToPolar(gx,gy, angleInDegrees=True)

face_detect = dlib.get_frontal_face_detector()

rects = face_detect(gray,1)

for (i,rect) in enumerate(rects):
  (x, y, w, h) = face_utils.rect_to_bb(rect)
  box = source[y:y+h, x:x+w]
  box = cv2.GaussianBlur(box,(23,23),30)

  blurred[y:y+box.shape[0], x:x+box.shape[1]] = box

plt.figure(figsize=(12,8))
plt.imshow(blurred)
plt.show()
