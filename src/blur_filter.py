import cv2
import numpy as np


def blur_mtcnn(source,faces):
  #create a temp image and a mask to work on
  temp_img = source.copy()
  maskShape = (source.shape[0], source.shape[1],1)
  mask =  np.full(maskShape,0, dtype=np.uint8)

  for i in range(len(faces)):
    # get dimensions for detect face
    x1, y1, width, height = faces[i]['box']
    x2, y2 = x1 + width, y1 + height

    # blur first so that the circle is not blurred
    temp_img[y1:y2,x1:x2] = cv2.GaussianBlur(temp_img[y1:y2,x1:x2],(99,99),30)

    # center and radius values
    cenX = (x1+x2)//2
    cenY = (y1+y2)//2
    radius = height//2

    # create the circle in the mask and in the tempImg, notice the one in the mask is full
    cv2.circle(temp_img,(cenX,cenY),radius,(0,255,0),5)
    cv2.circle(mask,(cenX,cenY),radius,(255),-1)
    
  #apply mask and save
  mask_inv = cv2.bitwise_not(mask)
  img1_bg = cv2.bitwise_and(source,source,mask = mask_inv)
  img2_fg = cv2.bitwise_and(temp_img, temp_img, mask = mask)
  dst = cv2.add(img1_bg,img2_fg)
  
  return dst
