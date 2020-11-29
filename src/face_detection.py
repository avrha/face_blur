import cv2
from mtcnn import MTCNN
from src.blur_filter import blur_mtcnn

# Used for processing images
def image(arg1,arg2):
  # Read in image
  img = cv2.imread(arg1,1)

  # Ensure file is opened
  if img is None:
    print("Could not open file")
    exit()

  # Use face detection
  detector = MTCNN()
  faces = detector.detect_faces(img)
  
  # Blur faces
  blur_mtcnn(img,faces)

  # Display image with blur
  cv2.imshow("Output",img)
  cv2.imwrite(arg2,img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


def video(arg1,arg2):
  # Capture video source
  cap = cv2.VideoCapture(arg1)

  # Ensure source is open
  if not cap.isOpened():
    print("Could not open file")
    exit()

  # Set dimensions for output file
  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))
  out = cv2.VideoWriter(arg2,cv2.VideoWriter_fourcc('M','J','P','G'),24,(frame_width,frame_height))

  while cap.isOpened():
    ret, frame = cap.read()

    # Failsafes for ret and frame
    if not ret:
      print("Error with ret")
      exit()
    
    if frame is None:
      print("Error with frame")
      exit()
    
    # Load DNN model and then detect face
    detector = MTCNN()
    faces = detector.detect_faces(frame)
    blur_mtcnn(frame,faces)
    out.write(frame)
    cv2.imshow("Real-time face detection", frame)

    # Press q to exit video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
