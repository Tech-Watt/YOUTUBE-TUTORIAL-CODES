import cv2 as cv
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv.VideoCapture(0)
hd = HandDetector(detectionCon=0.7)

width,height = 640,480
cap.set(3,width)
cap.set(4,height)

ball = cv.imread('ball.png',cv.IMREAD_UNCHANGED)
bat = cv.imread('speech.png',cv.IMREAD_UNCHANGED)
gameover = cv.imread('gameover.png',cv.IMREAD_UNCHANGED)

ball = cv.resize(ball,(40,40))
bat = cv.resize(bat,(120,26))
gameover = cv.resize(gameover,(width,height))

position = [50,50]
speedx = 15
speedy = 15
score = 0

while True:
    ret,img = cap.read()

    cv.rectangle(img,(0,480),(640,0),(0,0,255),8)
    cv.rectangle(img, (0, 440), (640, 480), (0, 255, 255), 6)

    hands,img = hd.findHands(img,flipType=True)
    if hands:
        bbox = hands[0]['bbox']
        x,y,w,h = bbox
        h1,w1,c = bat.shape
        x1 = x-h1//2
        x1 = np.clip(x1, 5, 510)
        img = cvzone.overlayPNG(img,bat,[x1,447])

        if position[1] < 50:
            speedy = -speedy
            position[0] -= 10

        if x1-10 < position[0] < x1 + w1 and 380 < position[1] < 380+h1:
            speedy = -speedy
            position[0] += 30
            score += 1

    if position[1] > 400:
        img = gameover
        cvzone.putTextRect(gameover,'Final score ' + str(score),[300,190],1.9,2,colorR=(0,0,0))
        cvzone.putTextRect(gameover, 'Press R to restart', [290, 305], 1.82, 2, colorR=(0, 0, 0))
        cvzone.putTextRect(gameover, 'Press Esc to quit', [290, 345], 1.82, 2, colorR=(0, 0, 0))

    else:
        if position[0] >=560 or position[0] <=20:
            speedx = -speedx

        position[0] += speedx
        position[1] += speedy
    cvzone.putTextRect(img,'Score '+str(score),[270,30],1.5)
    img = cvzone.overlayPNG(img,ball,position)


    cv.imshow('frame',img)
    key = cv.waitKey(1)
    if key == ord('r') or key == ord('R'):
        position = [50, 50]
        speedx = 15
        speedy = 15
        score = 0
        gameover = cv.resize(gameover, (width, height))

    else:
        if key == 27:
            break


