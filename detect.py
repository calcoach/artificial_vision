import cv2
import numpy as np

cam = cv2.VideoCapture(1)
kernel = np.ones((1, 1), np.uint8)

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    range_min = np.array([0, 211, 60])
    range_max = np.array([114, 255, 255])

    mascara = cv2.inRange(hsv, range_min, range_max)
    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

    x, y, w, h = cv2.boundingRect(opening)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("camara", frame)
    cv2.imshow("mascara", opening)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
