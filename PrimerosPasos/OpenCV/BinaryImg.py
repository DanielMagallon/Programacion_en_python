import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen = cv2.imread('perroSm.jpg',0)
mitad,imagen = cv2.threshold(imagen,255/2,255,cv2.THRESH_BINARY)

imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(imagen))

lbl = tk.Label(root)
lbl['image']=imgSmaller
lbl.pack()

root.mainloop()
