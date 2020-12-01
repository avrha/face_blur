# face_blur
Detects and blurs any faces in a given image or video.
<img width=800px src="https://github.com/avrha/face_blur/blob/main/examples/img_example.jpg/">
<img width=320px height=180 src= "https://github.com/avrha/face_blur/blob/main/examples/vid_example.gif/">
## Dependencies 
- Python3
- OpenCV
- Tensorflow
- MTCNN

### Install Dependencies
```
pip3 install -r ./requirements.txt
```

## Instructions
face_blur is a python script that takes in two arguments upon execution. First is the input file you wish to blur (flagged as  -i) and the second is the output file you wish to write to (flagged as -o). face_blur supports all video and file formats for processing. 

###  Blurring an Image 
``
python3 face_blur.py -i image.jpg -o image_blurred.jpg
``
### Resize an Image
The input image can be resized to improve performance during processing. Use the resize argument (flagged as -r) to shrink the image. The argument value is the percent change in size. 
``
# Resize image by 25 percent
python3 face_blur.py -i image.jpg -o image_resized_blurred.jpg -r 25
``

### Blurring an Video 
``
python3 face_blur.py -i video.mp4 -o video_blurred.mp4
``
### Skip Frames
Frames can be skipped to improve performance during processing. Use the skip frame argument (flagged as -s) to reduce the number of frames for processing. The argument value indicates how frequently to skip a frame.
``
# Skip frame every 10nth time
python3 face_blur.py -i video.mp4 -o video_skipped_blurred.mp4 -s 10
``
