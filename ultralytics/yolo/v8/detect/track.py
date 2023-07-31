from ultralytics import YOLO

fire-TW = "https://www.youtube.com/watch?v=RLcl-iePBuQ"
fire-USA = "https://www.youtube.com/watch?v=gOeptXATZMY"
car = "test/image/car.jpg"
cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"

model = YOLO('yolov8n.pt')

results = model.track(source=cctv, show=True)

#results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True, tracker="bytetrack.yaml")

