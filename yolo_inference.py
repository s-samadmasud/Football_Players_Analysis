from ultralytics import YOLO 

model = YOLO("models\\best.pt")  # Use double backslashes

results = model.predict('input_videos\sample_video.mp4',save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)