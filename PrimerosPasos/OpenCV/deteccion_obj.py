import cv2

imagen = cv2.imread('perroSm.jpg')
#imagen = cv2.cvtColor(imagen,4)

imagen2 = cv2.imread('minicara.png')
#imagen2 = cv2.cvtColor(imagen2,4)

metodo = cv2.TM_CCOEFF
#Mapa de calor
resultado = cv2.matchTemplate(imagen,imagen2,metodo)
cv2.imwrite('calorObj.jpg',resultado)

valor_min,valor_max,pos_min,pos_max = cv2.minMaxLoc(resultado)

alto,ancho,colores = imagen2.shape

top_izq = pos_max
bottom_derecha = (pos_max[0]+ancho,pos_max[1]+alto)

cv2.rectangle(imagen,top_izq,bottom_derecha, (255,0,0),8)

while True:

    cv2.imshow('My image',imagen)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imwrite('caraDetect.jpg',imagen)

