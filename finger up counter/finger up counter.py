import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
import os
import cvzone
fps = cvzone.FPS()

cap = cv2.VideoCapture(0)
cap.set(10,200)

hd = HandDetector(detectionCon=0.6)


overlaylist=[]
folderpath = 'Fingers'
list = os.listdir(folderpath)
print(folderpath)
for imgpath in list:
    image = cv2.imread(f'{folderpath}/{imgpath}')
    overlaylist.append(image)



while True:
    _, img = cap.read()
    fps.update(img,pos=(490,40),scale=2,color=(0,0,255))
    hand,imgs = hd.findHands(img)
    if hand:
        lefthand = hand[0]
        bbox = lefthand["bbox"]
        lmlist = lefthand['lmList']
        handtype = lefthand['type']
        fingersup = hd.fingersUp(lefthand)
        totalfingers = fingersup.count(1)
        h, w, c = overlaylist[totalfingers - 1].shape
        img[0:h, 0:w] = overlaylist[totalfingers - 1]
        cv2.rectangle(img, (0, 200), (170, 425), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, str(totalfingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 9, (255, 0, 0), 24)
        print(totalfingers)




    cv2.imshow('FRAME',img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()