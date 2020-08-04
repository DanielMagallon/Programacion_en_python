import numpy as np
import cv2

rostro1 = cv2.imread('rostro1.png')
familia = cv2.imread('familia.png')

cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectFace(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)

    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)

    return imagen1

cascada_eyes = cv2.CascadeClassifier('haarcascade_eye.xml'
                                     '')
def detectEyes(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_eyes.detectMultiScale(imagen1)

    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)

    return imagen1

#resultado = detectFace(familia); name='rostroDetect.png'
resultado = detectEyes(rostro1); name='eyesDetect.png'

while True:

    cv2.imshow('Face detection', resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.imwrite(name,resultado)



