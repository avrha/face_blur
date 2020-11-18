import cv2
import dlib
from hogBlur import face_blur


def main():
    img = cv2.imread('../../media/groupPic.jpg', 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detect = dlib.get_frontal_face_detector()
    faces = face_detect(gray, 1)
    face_blur(img, faces)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
