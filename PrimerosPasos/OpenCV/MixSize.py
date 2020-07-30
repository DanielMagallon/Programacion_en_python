import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen1 = cv2.imread('perroSm.jpg')
imagen1 = cv2.cvtColor(imagen1,cv2.COLOR_BGR2RGB)

watermark = cv2.imread("logo-redaitcursos.jpg")
watermark = cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
watermark = cv2.resize(watermark,(600,100))

part1 = imagen1[:100]
mixed_part = cv2.addWeighted(src1=part1,alpha=0.5,src2=watermark,beta=0.5,gamma=0)
imagen1[:100] = mixed_part
imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(imagen1))

tk.Label(root, image=imgSmaller).pack()
#tk.Label(root, image=ImageTk.PhotoImage(image=Image.fromarray(mixed_part))).pack()

root.mainloop()
