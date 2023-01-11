import cv2
import cvzone
import numpy as np

img = cv2.imread('cube.png')
imgblur = cv2.GaussianBlur(img,(3,3),3)
imgdil = cv2.dilate(imgblur,(5,5),1)

def empty(a):
    pass

cv2.namedWindow('trackcolor')
cv2.resizeWindow('trackcolor',(300,80))
cv2.createTrackbar('lower','trackcolor',0,255,empty)
cv2.createTrackbar('upper','trackcolor',0,255,empty)


while 1:
    blank = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    lower = cv2.getTrackbarPos('lower', 'trackcolor')
    upper = cv2.getTrackbarPos('upper', 'trackcolor')

    imgcanny = cv2.Canny(imgdil,lower,upper)
    contours,hierachy = cv2.findContours(imgcanny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(blank, contours, -1, (0, 0, 255), 2)

    allimg = cvzone.stackImages([img,imgcanny,blank],3,0.80)

    cv2.imshow('frame',allimg)
    cv2.waitKey(1)