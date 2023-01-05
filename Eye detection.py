import cv2
from cvzone.PoseModule import PoseDetector


cap = cv2.VideoCapture(0)

pd = PoseDetector()

while 1:
    ret,img = cap.read()
    pd.findPose(img,draw=0)

    lmlist , bbox = pd.findPosition(img,draw=0)
    if len(lmlist)!= 0:

        # right eye
        righ_eye = lmlist[5]
        rx,ry = righ_eye[1:-1]
        cv2.circle(img,(rx,ry),10,(0,0,255),-1)
        # left eye
        left_eye = lmlist[2]
        lx, ly = left_eye[1:-1]
        cv2.circle(img, (lx, ly), 10, (0, 0, 255), -1)




    cv2.imshow('frame',img)
    cv2.waitKey(1)