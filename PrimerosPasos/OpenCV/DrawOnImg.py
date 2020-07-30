import numpy as np
import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen = np.zeros(shape=(700,700,3),dtype=np.uint8)
cv2.rectangle(imagen,pt1=(20,20),pt2=(100,100),color=(255,0,0),thickness=10)
cv2.rectangle(imagen,pt1=(50,50),pt2=(80,80),color=(0,255,0),thickness=10)
cv2.rectangle(imagen,pt1=(120,120),pt2=(80,80),color=(0,0,255),thickness=10)
cv2.circle(imagen,center=(250,250),radius=135,color=(255,255,255),thickness=2)
cv2.line(imagen,pt1=(255,0),pt2=(255,500),color=(255,120,120))
fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(imagen,text="Hola prros",org=(20,100),fontFace=fuente,fontScale=3,
            color=(255,255,120),thickness=5,lineType=cv2.LINE_8)
cv2.putText(imagen,text="Adios",org=(70,220),fontFace=fuente,fontScale=5,
            color=(255,255,120),thickness=5,lineType=cv2.LINE_AA)

vertices = np.array([[100,300],[300,200],[400,400]],dtype=np.int32)
puntos = vertices.reshape(-1,1,2)

cv2.polylines(imagen,[puntos],isClosed=True,color=(255,255,255),thickness=4)



imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(imagen))

tk.Label(root, image=imgSmaller).pack()

root.mainloop()