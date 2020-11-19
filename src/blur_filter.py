import cv2

def blur_dnn(source, face):
  for idx, f in enumerate(face):
    # retrieve dimensions on detected face
    (startX, startY) = f[0], f[1]
    (endX, endY) = f[2], f[3]
                                                                          
    # create object based on retrieved dimensions
    box = source[startY:endY, startX:endX]
    box = cv2.GaussianBlur(box,(99,99),30)
    # overlay object on frame
    source[startY:startY + box.shape[0], startX:startX + box.shape[1]] = box 

def blur_cnn(source,faces):
  for faceRect in faces:
    # retrieve dimensions on detected face
    rect = faceRect.rect
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    # create object based on retrieved dimensions
    box = source[y:y+h, x:x+w]
    box = cv2.GaussianBlur(box,(99,99),30)
    # overlay object on frame
    source[y:y+box.shape[0], x:x+box.shape[1]] = box
