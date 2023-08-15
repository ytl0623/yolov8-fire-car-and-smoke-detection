from ultralytics import YOLO
from PIL import Image
import cv2
import torch

from send_email import send_email

from multiprocessing import Process

cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"
test_image = "test1.jpg"  # test2.jpg

model = YOLO( "best.pt" )

results = model( source = cctv, stream = True,  show = True, conf = 0.5 )

for r in results:
    try:    
        # detected fire confidence bigger than 0.8
        if r.boxes.conf[0] > torch.tensor([0.8]).cuda() :
            print("\nWarning Fire\n")
            p1 = Process( target = send_email )
            p1.start()
            break
        # detected fire and smoke at the same time
        elif ( torch.tensor([0.]).cuda() in r.boxes.cls ) and ( torch.tensor([1.]).cuda() in r.boxes.cls ) :
            print("\nWarning Fire\n")
            p1 = Process( target = send_email )
            p1.start()
            break
        # predicted, but no match confidece or class name
        else :
            #print("\nnothing\n")
            pass
    except :  # no predicted
        #print("\nnothing\n")
        pass
