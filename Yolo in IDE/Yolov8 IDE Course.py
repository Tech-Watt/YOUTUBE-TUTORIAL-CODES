from ultralytics import YOLO
import cvzone
import cv2
import math

# For images
# model = YOLO('yolov8n.pt')
# result = model('fellix.jpeg',show= True)
# cv2.waitKey(0)





# Running real time from webcam
cap = cv2.VideoCapture(0)
model = YOLO('Yolo-Weights/yolov8n.pt')


# Reading the classes
classnames = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()


while True:
    ret,frame = cap.read()
    result = model(frame,stream=True)

    # Getting bbox,confidence and class names informations to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            Class = int(box.cls[0])
            if confidence > 55:
                x1,y1,x2,y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,255),2)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 - 12],
                                   scale=1.5,thickness=2)




    cv2.imshow('frame',frame)
    cv2.waitKey(1)