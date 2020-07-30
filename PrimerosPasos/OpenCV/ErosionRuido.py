import cv2
import tkinter as tk
import numpy as np


from matplotlib import pyplot as plt
from PIL import Image, ImageTk

root = tk.Tk()

imagen = np.zeros((300,600))
#imagen = cv2.imread('perroSm.jpg',0)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen,text='ABCDE',org=(50,200),fontFace=font,fontScale=5,color=(255,255,255),thickness=8)

imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(imagen))

nucleo = np.ones((5,5),dtype=np.uint8)
imagen1 = cv2.erode(imagen,nucleo,iterations=1)

imgSmaller2 = ImageTk.PhotoImage(image=Image.fromarray(imagen1))
tk.Label(root, image=imgSmaller).pack()
#tk.Label(root, image=imgSmaller2).pack()

canvas2 = tk.Canvas(root, height=300, width=600)
canvas2.pack()


#ruido = np.random.randint(low=0,high=2,size=(300,600),dtype='uint8')
#ruido = ruido * 255
#imagen_ruido = imagen + ruido
#img = ImageTk.PhotoImage(image=Image.fromarray(imagen_ruido))
#canvas2.create_image(0, 0, anchor="nw", image=img)

#imagen_sin_ruido = cv2.morphologyEx(imagen,cv2.MORPH_OPEN,nucleo)
#img = ImageTk.PhotoImage(image=Image.fromarray(imagen_sin_ruido))
#canvas2.create_image(0, 0, anchor="nw", image=img)

gradiente = cv2.morphologyEx(imagen,cv2.MORPH_GRADIENT,nucleo)
img = ImageTk.PhotoImage(image=Image.fromarray(gradiente))
canvas2.create_image(0, 0, anchor="nw", image=img)

root.mainloop()
