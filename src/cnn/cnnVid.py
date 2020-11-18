# Todo
# Argument support
# Modularize code

import cv2
import dlib
import argparse
from imutils import face_utils
from cnnBlur import face_blur 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input file")
ap.add_argument("-s", "--skip", type=int,default=1,help="skip value")
args = vars(ap.parse_args())


def main():
    cap = cv2.VideoCapture(args["input"])
    cnnFaceDetector = dlib.cnn_face_detection_model_v1('../../model/mmod_human_face_detector.dat')
    
    if cap.isOpened() == 0:
        print("Error opening the video file")
    
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.resize(gray, (0, 0), fx=0.25, fy=0.25)
    
        if ret == 1:
            # skip frame
            if cap.get(1) % args["skip"] == 0:
                faces = cnnFaceDetector(gray, 1)
                print("Frame:",cap.get(1)) 

                face_blur(frame, faces)
    
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
