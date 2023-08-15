# Deep Learning-Based Fire Vehicle Detection and Real-Time Warning System
You can run code with your own PC/Notebook/... or on Google Colab.
<a href="https://colab.research.google.com/github/ytl0623/monai_wholeBody_ct_segmentation/blob/master/monai_wholeBody_ct_segmentation.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>

## Create a virtual environment
```
conda create -n [NAME] python==3.9
```

## Start the environment
```
conda activate [NAME]
```

## Clone Repository
```
git clone https://github.com/ytl0623/yolov8-fire-car-and-smoke-detection.git
```

## Go to the cloned folder
```
cd yolov8-fire-car-and-smoke-detection
```

## Install the dependencies
```
pip install -r requirements.txt
```

## Go to the working directory
```
cd ultralytics\yolo\v8\detect
```

## Execute inference
Change the input of the image/video/rtsp/..., what ever you want.
```
python main.py
```

## Results
The output image is like the below.

#![Download DICOM directory](https://github.com/ytl0623/monai_wholeBody_ct_segmentation/assets/55120101/3a606842-88c0-4253-9072-0c5c7e2d89ee)


## Reference
- https://github.com/ultralytics/ultralytics
- https://github.com/gaiasd/DFireDataset
- https://github.com/open-mmlab/mmyolo