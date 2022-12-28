import cv2
from cvzone.PoseModule import PoseDetector
import math
import numpy as np

cap = cv2.VideoCapture('train.MOV')
detector = PoseDetector(detectionCon=0.7,trackCon=0.7)



# Creating Angle finder class
class angleFinder:
    def __init__(self,lmlist,p1,p2,p3,p4,p5,p6,drawPoints):
        self.lmlist = lmlist
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.drawPoints = drawPoints
    #    finding angles

    def angle(self):
        if len(self.lmlist) != 0:
            point1 = self.lmlist[self.p1]
            point2 = self.lmlist[self.p2]
            point3 = self.lmlist[self.p3]
            point4 = self.lmlist[self.p4]
            point5 = self.lmlist[self.p5]
            point6 = self.lmlist[self.p6]

            x1,y1 = point1[1:-1]
            x2, y2 = point2[1:-1]
            x3, y3 = point3[1:-1]
            x4, y4 = point4[1:-1]
            x5, y5 = point5[1:-1]
            x6, y6 = point6[1:-1]

            # calculating angle for left and right hands
            leftHandAngle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                         math.atan2(y1 - y2, x1 - x2))

            rightHandAngle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                                          math.atan2(y4 - y5, x4 - x5))

            leftHandAngle = int(np.interp(leftHandAngle, [-170, 180], [100, 0]))
            rightHandAngle = int(np.interp(rightHandAngle, [-50, 20], [100, 0]))

            # drawing circles and lines on selected points
            if self.drawPoints == True:
                cv2.circle(img, (x1, y1), 10, (0, 255, 255), 5)
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), 6)
                cv2.circle(img, (x2, y2), 10, (0, 255, 255), 5)
                cv2.circle(img, (x2, y2), 15, (0, 255, 0), 6)
                cv2.circle(img, (x3, y3), 10, (0, 255, 255), 5)
                cv2.circle(img, (x3, y3), 15, (0, 255, 0), 6)
                cv2.circle(img, (x4, y4), 10, (0, 255, 255), 5)
                cv2.circle(img, (x4, y4), 15, (0, 255, 0), 6)
                cv2.circle(img, (x5, y5), 10, (0, 255, 255), 5)
                cv2.circle(img, (x5, y5), 15, (0, 255, 0), 6)
                cv2.circle(img, (x6, y6), 10, (0, 255, 255), 5)
                cv2.circle(img, (x6, y6), 15, (0, 255, 0), 6)

                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),4)
                cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)
                cv2.line(img, (x4, y4), (x5, y5), (0, 0, 255), 4)
                cv2.line(img, (x5, y5), (x6, y6), (0, 0, 255), 4)
                cv2.line(img, (x1, y1), (x4, y4), (0, 0, 255), 4)

            return list([leftHandAngle,rightHandAngle])

# defining some variables
counter = 0
direction = 0

while True:
    ret, img = cap.read()
    img = cv2.resize(img,(640,480))

    detector.findPose(img,draw=0)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=0,draw=False)

    angle1 = angleFinder(lmList,11,13,15,12,14,16,drawPoints=True)
    hands = angle1.angle()
    left, right = hands[0:]

    # Counting number of shoulder ups
    if left >= 90 and right >= 90:
        if direction == 0:
            counter += 0.5
            direction = 1
    if left <= 70 and right <= 70:
        if direction == 1:
            counter += 0.5
            direction = 0



    #putting scores on the screen
    cv2.rectangle(img,(0,0),(120,120),(255,0,0),-1)
    cv2.putText(img,str(int(counter)),(1,70),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.6,(0,0,255),6)

    # Converting values for rectangles
    leftval = np.interp(left,[0,100],[400,200])
    rightval = np.interp(right, [0, 100], [400, 200])

    # For color changing
    value_left = np.interp(left, [0, 100], [0, 100])
    value_right = np.interp(right,  [0, 100], [0, 100])

    # Drawing right rectangle and putting text
    cv2.putText(img,'R',(24,195),cv2.FONT_HERSHEY_DUPLEX,1,(255, 0, 0),5)
    cv2.rectangle(img,(8,200),(50,400),(0,255,0),5)
    cv2.rectangle(img, (8, int(rightval)), (50, 400), (255, 0, 0), -1)


    # Drawing right rectangle and putting text
    cv2.putText(img, 'L', (604,195),cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0),5)
    cv2.rectangle(img, (582, 200), (632, 400), (0, 255, 0), 5)
    cv2.rectangle(img, (582, int(leftval)), (632, 400), (255, 0, 0), -1)

    if value_left > 70:
        cv2.rectangle(img, (582, int(leftval)), (632, 400), (0, 0, 255), -1)

    if value_right > 70:
        cv2.rectangle(img, (8, int(rightval)), (50, 400), (0, 0, 255), -1)



    cv2.imshow("Image",img)
    cv2.waitKey(1)

