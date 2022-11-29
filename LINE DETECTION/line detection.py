import cv2 as cv
import numpy as np
import cvzone


video = cv.VideoCapture('road.mp4')


while 1:
    ret,vid = video.read()
    vid = cv.resize(vid, (640, 480))

    blur = cv.GaussianBlur(vid,(3,3),1)
    hsv = cv.cvtColor(blur,cv.COLOR_BGR2HSV)

    lower = np.array([18,100,140])
    higher = np.array([60, 255, 255])
    mask = cv.inRange(hsv, lower, higher)
    canny = cv.Canny(mask,90,100)

    lines = cv.HoughLinesP(canny,1,np.pi/180,50,maxLineGap = 60)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2  = line[0]
            cv.line(vid,(x1,y1),(x2,y2),(0,0,255),6)

    all = cvzone.stackImages([vid,hsv,mask,canny],2,0.65)
    cv.imshow('frame',all)
    cv.waitKey(30)