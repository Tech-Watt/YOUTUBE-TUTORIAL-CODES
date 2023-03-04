import cv2
import cvzone
from pyzbar import pyzbar as bar

cap = cv2.VideoCapture(0)
OUTPUT = None
while 1:
    ret,frame = cap.read()

    result = bar.decode(frame)
    for data in result:
        OUTPUT = data.data
        print(data.data)

    cvzone.putTextRect(frame,'Barcode Scanner',[190,30],thickness=2,scale=2,border=2)
    cvzone.putTextRect(frame, f'{OUTPUT}', [40, 300], thickness=2, scale=2, border=2)
    OUTPUT = None

    cv2.imshow('frame',frame)
    cv2.waitKey(1)
