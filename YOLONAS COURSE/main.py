import numpy as np
from super_gradients.training import models
import torch
import cv2
import cvzone
import math
import numpy


# IMAGES
# device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# model = models.get('yolo_nas_s',pretrained_weights='coco').to(device)
# output = model.predict('test2.jpg',conf=0.50)
# output.show()

# For Videos
cap = cv2.VideoCapture('video2.mp4')
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = models.get('yolo_nas_s',pretrained_weights='coco').to(device)

classnames = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()

while 1:
    rt,video = cap.read()
    video = cv2.resize(video,(1080,740))

    result = model.predict(video,conf=0.50)[0]
    bboxs = result.prediction.bboxes_xyxy
    confidence = result.prediction.confidence
    labels = result.prediction.labels

    for (bboxs,confidence,labels) in zip(bboxs,confidence,labels):
        x1,y1,x2,y2 = np.array((bboxs))
        x1, y1, x2, y2 = int(bboxs[0]),int(bboxs[1]),int(bboxs[2]),int(bboxs[3]),
        confidence = math.ceil(confidence*100)
        labels = int(labels)
        classdetect = classnames[labels]
        w,h = x2-x1,y2-y1
        cvzone.cornerRect(video,(x1,y1,w,h))
        cvzone.putTextRect(video,f'{classdetect} {confidence}%',
                           [x1+8,y1-12],scale=2)



    cv2.imshow('frame',video)
    cv2.waitKey(1)