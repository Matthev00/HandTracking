import cv2
import mediapipe as mp
import numpy as np
import time
import HandTrackingModule as htm


def putFps(img, pTime):
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(
        img, f'FPS: {int(fps)}', (40, 50),
        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
    return img, pTime


def drawCircle(p):
    x, y = p[1], p[2]
    cv2.circle(img, (x, y), 10, (255, 0, 0), cv2.FILLED)


def drawLine(p1, p2):
    x1, y1 = p1[1], p1[2]
    x2, y2 = p2[1], p2[2]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.HandDetector(detectionCon=0.8)


while True:
    succes, img = cap.read()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist):
        """
        lm no.4 tip of thumb
        lm no.8 tip of the index finger
        """
        drawCircle(lmlist[4])
        drawCircle(lmlist[8])
        drawLine(lmlist[4], lmlist[8])

    img, pTime = putFps(img, pTime)
    cv2.imshow('Img', img)
    cv2.waitKey(1)
