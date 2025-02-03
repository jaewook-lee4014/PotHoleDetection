from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='pothole_v8.yaml',
   imgsz=1280,
   epochs=20,
   batch=16,
   name='yolov8n_v8_50e'
)