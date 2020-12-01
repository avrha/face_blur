import cv2


def blur_mtcnn(source,faces):
  for i in range(len(faces)):
    # get dimensions for detect face 
    x1, y1, width, height = faces[i]['box']
    x2, y2 = x1 + width, y1 + height

    # create object based on retrieved dimensions
    box = source[y1:y2,x1:x2]

    # blur the object
    try:
      box = cv2.GaussianBlur(box,(99,99),30)
    except:
      break

    # overlay object on frame
    source[y1:y1+box.shape[0],x1:x1+box.shape[1]] = box
