import cv2
from sort import *
import math
import numpy as np
from ultralytics import YOLO
import cvzone

cap = cv2.VideoCapture('cars2.mp4')
model = YOLO('yolov8n.pt')

classnames  = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()

tracker = Sort(max_age=20)
line = [320,350,620,350]
counter = []

while 1:
    ret,frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('cars2.mp4')
        continue
    detections = np.empty((0,5))
    result = model(frame,stream=1)
    for info in result:
        boxes = info.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            conf = box.conf[0]
            classindex = box.cls[0]
            conf = math.ceil(conf * 100)
            classindex = int(classindex)
            objectdetect = classnames[classindex]

            if objectdetect == 'car' or objectdetect == 'bus' or objectdetect =='truck' and conf >60:
                x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
                new_detections = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections,new_detections))

                # cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
                # cvzone.putTextRect(frame,f'{objectdetect} {conf}%',
                #                    [x1+8,y1-12],thickness=2,scale=1.5)
                # print(classindex)

    track_result = tracker.update(detections)
    cv2.line(frame,(line[0],line[1]),(line[2],line[3]),(0,255,255),7)

    for results in track_result:
        x1,y1,x2,y2,id = results
        x1, y1, x2, y2, id = int(x1), int(y1), int(x2), int(y2),int(id)

        w,h = x2-x1,y2-y1
        cx,cy = x1+w//2 , y1+h//2

        cv2.circle(frame,(cx,cy),6,(0,0,255),-1)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
        cvzone.putTextRect(frame,f'{id}',
                           [x1+8,y1-12],thickness=2,scale=1.5)

        if line[0] < cx <line[2] and line[1] -20 <cy <line[1]+20:
            cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 15)
            if counter.count(id) == 0:
                counter.append(id)



    cvzone.putTextRect(frame,f'Total Vehicles ={len(counter)}',[290,34],thickness=4,scale=2.3,border=2)






    cv2.imshow('frame',frame)
    cv2.waitKey(1)