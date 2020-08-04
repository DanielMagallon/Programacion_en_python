import numpy as np
import cv2


cereal = cv2.imread('cereal.png')
cereales = cv2.imread('cereales.png')

sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(cereal,None)
kp2,des2 = sift.detectAndCompute(cereales,None)

indice = dict(algorithm=0,trees=5)
busqueda = dict(checks=50)

flan = cv2.FlannBasedMatcher(indice,busqueda)
emparejar = flan.knnMatch(des1,des2,k=2)

mejores = []

for e1,e2 in emparejar:

    if e1.distance < 0.7 * e2.distance:
        mejores.append([e1])

imagen_emp = cv2.drawMatchesKnn(cereal,kp1,cereales,kp2,mejores[0:30],None,flags=0)



while True:

    cv2.imshow('My image',imagen_emp)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.imwrite('emparejamiento.jpg',imagen_emp)