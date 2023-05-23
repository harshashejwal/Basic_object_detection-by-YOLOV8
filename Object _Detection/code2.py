
from ultralytics import YOLO

# Initialize the YOLO model
model = YOLO('yolov8n.pt')

results = model.predict(source='elon1.jpg', show=True, save = True)
