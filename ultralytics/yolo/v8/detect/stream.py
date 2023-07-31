import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
#model = YOLO( "yolov8n.pt" )
model = YOLO( "runs/detect/E/weights/best.pt" )

# Open the video file
fire_TW = "https://www.youtube.com/watch?v=RLcl-iePBuQ"
fire_USA = "https://www.youtube.com/watch?v=gOeptXATZMY"
car = "test_imgs/car.jpg"

# stop for ten seconds
cctv = "https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10000&0.8101103970745722&t1968=0.4780483205606241"

cap = cv2.VideoCapture( cctv )

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

