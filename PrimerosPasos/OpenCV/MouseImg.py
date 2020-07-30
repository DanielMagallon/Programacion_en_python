import cv2
import numpy as np

def draw(event,x,y,labels,parameters):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen,(x,y),50,(255,255,255),-1)

cv2.namedWindow(winname='my_img')
cv2.setMouseCallback('my_img',draw)


imagen = np.zeros((700,700,3),np.int8)

while True:

    cv2.imshow('my_img',imagen)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()