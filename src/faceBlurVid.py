import cv2
import dlib

def process(frame):
  cnnFaceDetector = dlib.cnn_face_detection_model_v1('../model/mmod_human_face_detector.dat')
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = cnnFaceDetector(gray,0)
  
  return faces

def skipFrame(capture):
  frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
  print(frame_count)

  for x in range(frame_count):
    if x % 5 == 0:
      capture.set(cv2.CAP_PROP_POS_FRAMES, x)
      _, frame = capture.read()
      return frame


def main():
  cap = cv2.VideoCapture('../media/groupVid.mp4')
  
  if(cap.isOpened() == 0):
    print("Error opening the video file")
  
  while(cap.isOpened()):
    frame = skipFrame(cap)
    faces = process(frame)
    for faceRect in faces:
      rect = faceRect.rect
      x = rect.left()
      y = rect.top()
      w = rect.right() - x
      h = rect.bottom() - y
  
      box = frame[y:y+h,x:x+w]
      box = cv2.GaussianBlur(box,(23,23),30)
      frame[y:y+box.shape[0], x:x+box.shape[1]] = box 
  
      cv2.imshow('Video',frame)
  
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    else:
      break
  
  cap.release()
  cv2.destroyAllWindows()
  return 0

if __name__ == "__main__":
  main()
