import cv2
import numpy as np

dibujando=False
valX = 0
valY = 0

def draw(event,x,y,labels,parameters):

    global dibujando,valY,valX

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valX = x
        valY = y
    elif event ==  cv2.EVENT_MOUSEMOVE:
        if dibujando:
            cv2.rectangle(imagen,(valX,valY),(x,y),(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valX, valY), (x, y), (0, 255, 0), -1)


name='my_img'
cv2.namedWindow(winname=name)
cv2.setMouseCallback(name,draw)


imagen = np.zeros((700,700,3),np.uint8)

while True:

    cv2.imshow(name,imagen)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()