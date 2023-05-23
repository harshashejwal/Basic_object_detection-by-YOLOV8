from ultralytics import YOLO

#yolo detect predictmodel="yolov8n.pt" source= "bikes (1).mp4" show=True
#model = YOLO("yolov8n.pt")

#results = model("bike.mp4")
model = YOLO('yolov8n.pt')
model.predict(source="tom.mp4")

#results = model('bike.mp4')

# Print the results
#results.print()