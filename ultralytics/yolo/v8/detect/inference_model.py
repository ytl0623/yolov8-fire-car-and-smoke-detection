from ultralytics import YOLO
from PIL import Image
import cv2
import torch

from send_email import send_email

fire_TW = "https://www.youtube.com/watch?v=RLcl-iePBuQ"
fire_USA = "https://www.youtube.com/watch?v=gOeptXATZMY"
car = "test_imgs/"
allTest = "all/"
cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"

model = YOLO( "runs/detect/H/weights/best.pt" )
#model = YOLO( "/home/ytl0623/data/Fire-Detection-using-YOLOv8/detect/models/best.pt" )
#model = YOLO( "yolov8n.pt" )

results = model( source = car, save = True, name = "H_predict" )
