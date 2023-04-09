import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto


cap = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)

while 1:
    rt,frame = cap.read()
    frame = cv2.resize(frame,(1080,720))
    cvzone.putTextRect(frame,'DINO GAME HACK',[360,40],scale=3,thickness=3,border=2)

    hand,frame = hd.findHands(frame)

    if hand:
        hands = hand[0]
        lmlist = hands['lmList']
        # print(lmlist)

        length,info , frame = hd.findDistance(lmlist[4][0:2],lmlist[8][0:2],frame)
        length = round(length)

        if length < 25:
            auto.press('up')


    cv2.imshow('frame',frame)
    cv2.waitKey(1)