import numpy as np
import cv2

imagen = cv2.imread('cara_perro.jpg')
imagen = cv2.blur(imagen,ksize=(5,5))
contorno = cv2.Canny(image=imagen,threshold1=127,threshold2=127)

while True:

    cv2.imshow('My image',contorno)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imwrite('contorno_cara.png',contorno)