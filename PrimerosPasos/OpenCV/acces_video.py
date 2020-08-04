import cv2

capture = cv2.VideoCapture(0)

ancho = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

code = cv2.VideoWriter_fourcc(*'MJPG')
recorder = cv2.VideoWriter('myvideo.avi',code,30,(ancho,altura))


while True:
    resultado,video = capture.read()

    recorder.write(video)

    cv2.imshow("my video",video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
recorder.release()
cv2.destroyAllWindows()
