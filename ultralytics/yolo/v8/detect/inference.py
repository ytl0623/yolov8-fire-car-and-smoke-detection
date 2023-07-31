from ultralytics import YOLO
from PIL import Image
import cv2
import torch

from send_email import send_email

fire_TW = "https://www.youtube.com/watch?v=RLcl-iePBuQ"
fire_USA = "https://www.youtube.com/watch?v=gOeptXATZMY"
car = "test_imgs/car2.jpg"
cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"

model = YOLO( "runs/detect/E/weights/best.pt" )
#model = YOLO( "/home/ytl0623/data/Fire-Detection-using-YOLOv8/detect/models/best.pt" )
#model = YOLO( "yolov8n.pt" )

#results = model( source = fire_USA, save = True, name = "E2", show = True )

results = model( source = cctv, stream = True,  show = True, classes = [0,1], conf = 0.8 )

# Need stream = True
for r in results:
    try:
        print( r.boxes )
        if r.boxes.cls == torch.tensor([0.]).cuda() and r.boxes.conf >= torch.tensor([0.8]).cuda() :
            print("\nWarning Smoke\n")
            send_email( 0 )
            break
        elif r.boxes.cls == torch.tensor([1.]).cuda() and r.boxes.conf >= torch.tensor([0.8]).cuda() :
            print("\nWarning Fire\n")
            send_email( 1 )
            break
        else :  # predicted, but no match confidece or class name
            print("\nnothing\n")
    
    except :  # no predicted
        print("\nnothing\n")

    



"""
    Args:
        orig_img (numpy.ndarray): The original image as a numpy array.
        path (str): The path to the image file.
        names (dict): A dictionary of class names.
        boxes (torch.tensor, optional): A 2D tensor of bounding box coordinates for each detection.
        masks (torch.tensor, optional): A 3D tensor of detection masks, where each mask is a binary image.
        probs (torch.tensor, optional): A 1D tensor of probabilities of each class for classification task.
        keypoints (List[List[float]], optional): A list of detected keypoints for each object.
"""

"""
boxes: tensor([[329.7507,  46.3922, 614.8512, 298.3295,   0.8464,   0.0000]], device='cuda:0')
cls: tensor([0.], device='cuda:0')
conf: tensor([0.8464], device='cuda:0')
data: tensor([[329.7507,  46.3922, 614.8512, 298.3295,   0.8464,   0.0000]], device='cuda:0')
id: None
is_track: False
orig_shape: (560, 800)
shape: torch.Size([1, 6])
xywh: tensor([[472.3009, 172.3608, 285.1005, 251.9373]], device='cuda:0')
xywhn: tensor([[0.5904, 0.3078, 0.3564, 0.4499]], device='cuda:0')
xyxy: tensor([[329.7507,  46.3922, 614.8512, 298.3295]], device='cuda:0')
xyxyn: tensor([[0.4122, 0.0828, 0.7686, 0.5327]], device='cuda:0')
"""










































