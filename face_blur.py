#import modules
import sys
import argparse
import cv2
import sys

from src.image import image
from src.video import video

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
