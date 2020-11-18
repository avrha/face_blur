import cv2
import dlib
import argparse
from hogBlur import face_blur

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input file")
ap.add_argument("-s", "--skip", type=int,default=1,help="skip value")
args = vars(ap.parse_args())

def main():
    img = cv2.imread(args["input"], 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detect = dlib.get_frontal_face_detector()
    faces = face_detect(gray, 1)
    face_blur(img, faces)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
