import cv2
import numpy as np

cam = cv2.VideoCapture(1)
kernel = np.ones((1, 1), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    range_min = np.array([0, 211, 60])
    range_max = np.array([114, 255, 255])

    mascara = cv2.inRange(hsv, range_min, range_max)
    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)

    contornos, hierachy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cont = 0;
    for contorno in contornos:
        x, y, w, h = cv2.boundingRect(contorno)

        if h > 60:
          cont += 1
          cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
          print("x: {} y : {} w: {} h: {} ".format(x, y, w, h))
          cv2.putText(frame,'Tomate {}'.format(cont),(x,y),font,1,(0,255,255),2,cv2.LINE_AA)

    cv2.putText(frame, 'Hay {} tomates'.format(cont), (200, 40), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("camara", frame)
    cv2.imshow("mascara", opening)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
