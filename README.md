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

##  Instructions
face_blur utilizes predefined arguments upon execution. Input (-i) and output (-o) are both required. Resize image (-r) and skip frame  (-s) are both optional. All video and image formats are supported. 

### Blur an Image
Use the input argument (-i) to specify the image to blur. Then use the output argument (-o) to specify a write to file. 
  
``
python3 face_blur.py -i image.jpg -o image_blurred.jpg
``
### Resize an Image
The input image can be resized to improve performance during processing. Use the resize argument (flagged as -r) to shrink the image. The argument value is the percent change in size. 

`python3 face_blur.py -i image.jpg -o image_resized_blurred.jpg -r 25`

### Blur a Video 
Use the input argument (-i) to specify the video to blur. Then use the output argument (-o) to specify a write to file. 

`python3 face_blur.py -i video.mp4 -o video_blurred.mp4`


### Skip Frames
Frames can be skipped to improve performance during processing. Use the skip frame argument (flagged as -s) to reduce the number of frames for processing. The argument value indicates how frequently to skip a frame.

`python3 face_blur.py -i video.mp4 -o video_skipped_blurred.mp4 -s 10`
