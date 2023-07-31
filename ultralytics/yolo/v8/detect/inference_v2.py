from ultralytics import YOLO
from PIL import Image
import cv2
import torch

from send_email import send_email

cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"

model = YOLO( "runs/detect/E/weights/best.pt" )

results = model( source = cctv, stream = True,  show = True, conf = 0.8 )

for r in results:
    try:
        # must bigger than 0.5
        if r.boxes.cls == torch.tensor([0.]).cuda() :
            print("\nWarning Smoke\n")
            send_email( 0 )
            break
        elif r.boxes.cls == torch.tensor([1.]).cuda() :
            print("\nWarning Fire\n")
            send_email( 1 )
            break
        else :  # predicted, but no match confidece or class name
            print("\nnothing\n")
    
    except :  # no predicted
        print("\nnothing\n")
