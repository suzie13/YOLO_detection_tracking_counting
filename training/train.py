# -*- coding: utf-8 -*-

!nvidia-smi

# clone darknet repo
!git clone https://github.com/AlexeyAB/darknet

# Commented out IPython magic to ensure Python compatibility.
# change makefile to have GPU and OPENCV enabled
# %cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

# Compile
!make

from google.colab import drive
drive.mount('/content/gdrive')
!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

# this creates a symbolic link so that now the path /content/gdrive/My\ Drive/ is equal to /mydrive
!ln -s /content/gdrive/My\ Drive/ /mydrive
!ls /mydrive

# Commented out IPython magic to ensure Python compatibility.
# cd back into the darknet folder to run detections
# %cd darknet

# this is where my datasets are stored within my Google Drive (I created a yolov4 folder to store all important files for custom training) 
!ls /mydrive/yolov4-tiny

# copy over both datasets into the root directory of the Colab VM (comment out test.zip if you are not using a validation dataset)
!cp /mydrive/yolov4-tiny/obj.zip ../
!cp /mydrive/yolov4-tiny/test.zip ../

# unzip the datasets and their contents so that they are now in /darknet/data/ folder
!unzip ../obj.zip -d data/
!unzip ../test.zip -d data/

# download cfg to google drive and change its name
#!cp cfg/yolov4-custom.cfg /mydrive/yolov4/yolov4-obj.cfg

# to download to local machine (change its name to yolov4-obj.cfg once you download)
#download('cfg/yolov4-custom.cfg')

# upload the custom .cfg back to cloud VM from Google Drive
!cp /mydrive/yolov4-tiny/yolov4-tiny-custom.cfg ./cfg

# upload the obj.names and obj.data files to cloud VM from Google Drive
!cp /mydrive/yolov4-tiny/obj.names ./data
!cp /mydrive/yolov4-tiny/obj.data  ./data

# upload the generate_train.py and generate_test.py script to cloud VM from Google Drive
!cp /mydrive/yolov4-tiny/generate_train.py ./
!cp /mydrive/yolov4-tiny/generate_test.py ./

!python generate_train.py
!python generate_test.py

# verify that the newly generated train.txt and test.txt can be seen in our darknet/data folder
!ls data/

# Download the yolov4-tiny pre-trained weights file
!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29


# Commented out IPython magic to ensure Python compatibility.
# define helper function imShow
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
#   %matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  #plt.show('')


# train your custom detector! (uncomment %%capture below if you run into memory issues or your Colab is crashing)
# %%capture
!./darknet detector train data/obj.data cfg/yolov4-tiny-custom.cfg yolov4-tiny.conv.29 -dont_show -map

# show chart.png of how custom object detector did with training
imShow('chart.png')

pwd

!./darknet detector map data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_1000.weights


#set your custom cfg to test mode 
# %cd cfg
!sed -i 's/batch=64/batch=1/' yolov4-tiny-custom.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov4-tiny-custom.cfg
# %cd ..

!./darknet detector test data/obj.data cfg/yolov4-tiny-custom.cfg /mydrive/yolov4-tiny/backup/yolov4-tiny-custom_best.weights /mydrive/yolov4-tiny/biker.jpg -thresh 0.5
imShow('predictions.jpg')

# run your custom detector on a video with this command (upload a video to your google drive to test, the thresh flag sets the minimum accuracy required for object detection).This saves the output video with the detections in your output path

!./darknet detector demo data/obj.data cfg/yolov4-tiny-custom.cfg /content/gdrive/MyDrive/yolov4-tiny/backup/yolov4-tiny-custom_best.weights -dont_show /mydrive/yolov4-tiny/Bike racing.mp4 -thresh 0.5 -i 0 -out_filename /mydrive/yolov4-tiny/result.avi