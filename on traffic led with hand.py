import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject
import pyautogui


cap = cv.VideoCapture(1)
cap.set(3,400)
cap.set(4,400)
hd = HandDetector(detectionCon=0.8 )
fd = FaceDetector()
data = SerialObject('COM3')
indexs = 0
def update(cursor,bboxs):
    global indexs
    for x,bbox in enumerate(bboxs):
        x1,y1,x2,y2 = bbox
        if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
            index = x+1
            indexs = index
            cv.rectangle(video, (x1, y1), (x2, y2), (255, 0, 0), -1)



while True:
    sucess,video = cap.read()
    # video,face = fd.findFaces(video)
    hands,video = hd.findHands(video)

    if hands:
        hand = hands[0]
        handtype = hand['type']
        lmlist  = hand['lmList']

        video, bbox0 = cvzone.putTextRect(video, 'TRAFFIC LIGHT CONTROL PANEL', (90, 50), border=5,scale=2,colorB=(0,0,0))
        video,bbox1 = cvzone.putTextRect(video,'RED',(90,180),border=5,colorB=(0,0,255),colorT=(0,0,255),colorR=(0,0,0),scale=1.6)
        video, bbox2= cvzone.putTextRect(video, 'YELLOW', (260,180), border=5,colorB=(0,255,255),colorT=(0,255,255),colorR=(0,0,0),scale=1.5)
        video, bbox3 = cvzone.putTextRect(video, 'GREEN', (470,180), border=5,colorB=(0,255,0),colorT=(0,255,0),colorR=(0,0,0),scale=1.5)
        video, bbox4 = cvzone.putTextRect(video, 'QUIT PROGRAM', (230, 410), border=5, colorB=(0, 0, 0),scale=1.7,colorT=(0,0,255),colorR=(0, 0, 0))
        video, bbox5 = cvzone.putTextRect(video, 'Reset', (295, 290), border=5, colorB=(90, 150, 78),scale=1.7,colorT=(254,0,255),colorR=(0, 0, 0))
        length, info, img = hd.findDistance(lmlist[8][0:2], lmlist[8][0:2], video)
        cursor = lmlist[8]
        if length < 24:
         update(cursor, [bbox1, bbox2, bbox3,bbox4,bbox5])
    # print(indexs)
    if indexs == 1:
        data.sendData([1])


    elif indexs == 2:
        data.sendData([2])

    elif indexs == 3:
        data.sendData([3])

    elif indexs == 4:
        data.sendData([4])
        pyautogui.press(27)


    elif indexs == 5:
        data.sendData([5])

    cv.imshow('frame',video)
    key = cv.waitKey(1)
    if key == 27:
        quit()
