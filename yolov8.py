from ultralytics import YOLO

model = YOLO('yolov8n.pt')##object detection

results = model(source= r"C:\Users\lenovo\Myenv\traffic_video.mp4", show=True, conf=0.4, save=True)
