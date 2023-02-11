import cv2 as cv
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv.VideoCapture(0)
fm = FaceMeshDetector()
rightEye =[463,414,286,258,257,259,260,467,359,255,339,254,253,252,256,341]
leftEye = [130,247,30,29,27,28,56,190,243,112,26,22,23,24,110,25]
rightEye.extend(leftEye)

while 1:
    _,frame = cap.read()
    frame, face = fm.findFaceMesh(frame,draw=0)

    if face != 0:
        all_marks = face[0]
        # print(len(all_marks))
        for i in rightEye:
            points = all_marks[i]
            cv.circle(frame,points,2,(0,0,255),2)

    elif face <= 0:
        pass

    cv.imshow('frame',frame)
    cv.waitKey(1)