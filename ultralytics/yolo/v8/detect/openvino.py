# https://docs.ultralytics.com/modes/export/

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official model
#model = YOLO('path/to/best.pt')  # load a custom trained

# Export the model
#model.export(format='coreml', device=0)
#model.export(format='saved_model', device=0)
model.export(format='pb', device=0)
model.export(format='tflite', device=0)
model.export(format='edgetpu', device=0)
model.export(format='tfjs', device=0)
model.export(format='paddle', device=0)
model.export(format='ncnn', device=0)
