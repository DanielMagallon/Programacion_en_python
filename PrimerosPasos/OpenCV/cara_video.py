import numpy as np
import cv2

cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectFace(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)

    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)

    return imagen1

capture = cv2.VideoCapture(0)


while True:

    resultado, video = capture.read()
    video = detectFace(video)
    cv2.imshow('Our video with rectanglle',video)

    tecla = cv2.waitKey(1)

    if tecla==27:
        break

capture.release()
cv2.destroyAllWindows()