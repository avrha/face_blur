import cv2
from mtcnn import MTCNN
from src.blur_filter import blur_mtcnn


# Used for processing images
def image(arg1,arg2):
  # Read in image
  img = cv2.imread(arg1,1)

  # Check file is opened
  if img is None:
    print("Could not open file")
    exit()

  # Face detection
  detector = MTCNN()
  faces = detector.detect_faces(img)
  
  # Blur faces
  blurred_image = blur_mtcnn(img,faces)

  # Display and write out image with blur
  blurred_resized = cv2.resize(blurred_image,(0,0),fx=0.50,fy=0.50)
  cv2.imshow("Image Output",blurred_resized)
  cv2.imwrite(arg2,blurred_image)

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

  # Output variable
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
    
    # Face Detection
    detector = MTCNN()
    faces = detector.detect_faces(frame)
    
    # Blur faces in frame 
    blurred_frame = blur_mtcnn(frame,faces)

    # Show and write out frame
    cv2.imshow("Video Output", blurred_frame)
    out.write(blurred_frame)

    # Press q to exit video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  cap.release()
  out.release()
  cv2.destroyAllWindows()
