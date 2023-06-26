from ultralytics import YOLO
import cv2 

model = YOLO('../Yolo-Weights/yolov8n.pt')
result = model("images/3.png" , show = True)
cv2.waitKey(0)
