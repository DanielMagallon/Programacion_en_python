import cv2

capture = cv2.VideoCapture(0)

ancho = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

#esquina izq rectangulo
x=300
y=300

#dimension
w = ancho // 4
h = altura // 4

while True:

    resultado, video = capture.read()

    cv2.rectangle(video,(x,y),(x+w,y+h),color=(255,0,0), thickness=4)

    cv2.imshow('Our video with rectanglle',video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()




