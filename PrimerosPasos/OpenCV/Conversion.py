import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen = cv2.imread('perroSm.jpg')
imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2HLS_FULL)


imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(imagen))

tk.Label(root, image=imgSmaller).pack()

root.mainloop()