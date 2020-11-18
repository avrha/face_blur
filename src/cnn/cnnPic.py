import sys
import cv2
from cnnBlur import face_blur
import dlib
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input file")
ap.add_argument("-s", "--skip", type=int,default=1,help="skip value")
args = vars(ap.parse_args())


def main():
    # Load in and convert source image to into grayscale
    img = cv2.imread(args["input"], 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.resize(gray, (0, 0), fx=0.25, fy=0.25)
    frame_count = 0
    face_count = 0

    # Detect faces using CNN model
    cnn_face_detector = dlib.cnn_face_detection_model_v1('../../model/mmod_human_face_detector.dat')
    faces = cnn_face_detector(gray, 1)

    # Blur faces
    face_blur(img, faces, frame_count, face_count)

    # Display image with blur
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    main()
