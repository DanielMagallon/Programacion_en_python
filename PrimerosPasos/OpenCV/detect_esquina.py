import numpy as np
import cv2

ajedrez = cv2.imread('tablero-ajedrez.png')
gray_chess = cv2.cvtColor(ajedrez,cv2.COLOR_BGR2GRAY)


esquinas = cv2.goodFeaturesToTrack(gray_chess,100,0.01,10)
esquinas = np.int0(esquinas)

for i in esquinas:
    x,y = i.ravel()
    cv2.circle(ajedrez,(x,y),4,(255,0,0),8)

while True:

    cv2.imshow('My image',ajedrez)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break