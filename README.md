# YOLO_detection_tracking_counting




Using the OIDv4-toolkit, we can download images along with its annotations from the 'Open Images Dataset' of Google using the below command:

`python main.py downloader --classes Helmet --type_csv train --limit 1000`


This will download from train subset and limit value can be altered


The results from training on 1000 images using yolov4-tiny are shown. The framework incorporated was tensorflow.

### Running detections and counting on image
# ![After detection + counting](https://user-images.githubusercontent.com/39700209/151843359-7d8eab1f-c570-4a5d-8e2b-cc1c46600429.png)















### Running detections and counting on video
https://user-images.githubusercontent.com/39700209/151848178-14013787-aa32-441f-9747-b5e92315f286.mp4

















### Running detections on a harder video:
https://user-images.githubusercontent.com/39700209/152034431-68237047-9332-4078-a963-a2eca93c98b8.mp4










FUTURE SCOPE:
>The model can be trained for more images by changing the --limit to a greater number.
>The algorithms YOLOv4 or YOLOv5 can be the alternative to be used for training.
>Different weights can be checked to find the one giving better results and avoiding the overfitted or undertrained one.


