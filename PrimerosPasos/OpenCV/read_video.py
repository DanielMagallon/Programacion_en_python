import cv2

capture = cv2.VideoCapture('myvideo.avi')

if not capture.isOpened():
    print('Error al abrir el fichero')

while capture.isOpened():

    resultado,video = capture.read()

    if resultado:

        cv2.imshow('My video',video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else: break

capture.release()
cv2.destroyAllWindows()
#exit(2)
