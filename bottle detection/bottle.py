import cv2 as cv
import cvzone
from ultralytics import YOLO
import math
from sort import *
import numpy as np


cap = cv.VideoCapture('bot1.mp4')
model = YOLO('yolov8l.pt')


tracker = Sort(max_age=20,min_hits=3)
line = [1100,0,1100,900]
counterin = []


classnames = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()


while 1:
    ret,img = cap.read()

    if not ret:
        cap = cv.VideoCapture('bot1.mp4')
        continue



    detections = np.empty((0, 5))


    results = model(img, stream=True)
    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = box.conf[0]
            class_detect = box.cls[0]
            class_detect = int(class_detect)
            class_detect = classnames[class_detect]
            conf = math.ceil(confidence * 100)
            if class_detect == 'bottle' and conf >= 80:
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                current_detections = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, current_detections))



    tracker_result = tracker.update(detections)
    cv.line(img, (line[0], line[1]), (line[2], line[3]), (0, 255, 255), 5)


    for track_result in tracker_result:
        x1, y1, x2, y2, id = track_result
        x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2), int(id)
        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2


        # cv.circle(img,(cx,cy),8,(0,255,255),-1)
        cvzone.cornerRect(img,[x1,y1,w,h],rt=5)
        cvzone.putTextRect(img, f'{id}', [x1 + 8, y1 - 12],
                           scale=2, thickness=2)


        if line[1] < cy < line[3] and line[2] - 10< cx < line[2] + 10:
            cv.line(img, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 10)
            if counterin.count(id) == 0:
                counterin.append(id)


    cvzone.putTextRect(img, f'Total Drinks = {len(counterin)}', [500, 34], thickness=4, scale=2.3, border=2)


    cv.imshow('frame',img)
    cv.waitKey(1)


