import cv2 as cv
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as gui

cap = cv.VideoCapture(0)
hd = HandDetector(detectionCon=0.70)

text = 'AI Virtual Scrolling'
while 1:
    ret,img = cap.read()
    cv.rectangle(img,(0,230),(640,250),(0,255,255),-1)
    cvzone.putTextRect(img,text,[130,40],border=2,colorB=(0,255,255),scale=2.5)
    hands,img = hd.findHands(img)

    if hands:
        bbox = hands[0]['bbox']
        x,y,w,h = bbox
        lmlist = hands[0]['lmList']
        length,info,img = hd.findDistance(lmlist[4][0:2],lmlist[8][0:2],img)
        print(length)

        if length < 20:
            if y > 190:
                gui.press('down')
            elif y < 180:
                gui.press('up')








    cv.imshow('frame',img)
    cv.waitKey(1)

