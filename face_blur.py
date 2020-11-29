#import modules
import argparse
import cv2
from src.face_detection import image, video


# add arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to image file")
ap.add_argument("-o", "--output", required=True, help="Name of output file")
args = vars(ap.parse_args())


def main():
  if cv2.haveImageReader(args["input"]) == True:
    image(args["input"],args["output"])

  else:
    print("this is a video file")
    video(args["input"],args["output"]) 

if __name__ == "__main__":
  main()
