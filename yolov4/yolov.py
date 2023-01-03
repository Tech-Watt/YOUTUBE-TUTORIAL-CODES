import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# loading the classes
classes = []
with open('classes.txt', 'r') as f:
    classes = f.read().splitlines()




# loading the yolo files
net = cv2.dnn.readNet('yolov4-tiny.weights','yolov4-tiny.cfg')

while 1:
    ret, image = cap.read()

    bbox = []
    confidence = []
    classIds = []

    image = cv2.resize(image,(640,480))
    width,height,c = image.shape
    blobImage = cv2.dnn.blobFromImage(image,1/255,(320,320),(0,0,0),swapRB = 1,crop = 0)
    net.setInput(blobImage)

    # loading output layers
    outputLayers = net.getUnconnectedOutLayersNames()
    out = net.forward(outputLayers)

    # getting bbox and other information
    for outs in out:
        for result in outs:
            score = result[5:]
            classId = np.argmax(score)
            confident = score[classId]

            if confident > 0.65:
                x1 = int(result[0]* width)
                y1 = int(result[1] * height)
                w = int(result[2]*width)
                h = int(result[3] * height)

                x = (x1 - w//2)
                y = (y1 - h//2)
                bbox.append([x,y,w,h])
                confidence.append(confident)
                classIds.append(classId)

    results = cv2.dnn.NMSBoxes(bbox,confidence,0.5,0.4)
    colors = np.random.uniform(0,255,size=len(bbox))

    for i in results:
        x,y,w,h = bbox[i]
        label = str(classes[classIds[i]])
        confi = str(round(confidence[i]*100,0))
        color = colors[i]

        cv2.rectangle(image,(x,y),(x+w,y+h),color,3)
        cv2.putText(image,label+' '+confi+'%',(x,y-10),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),1)


    cv2.imshow('frame',image)
    cv2.waitKey(1)