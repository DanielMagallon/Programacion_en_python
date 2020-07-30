import numpy as np
import matplotlib.pyplot as plt
import cv2
import tkinter as tk
from PIL import Image, ImageTk

im = cv2.imread(filename="perroSm.jpg")
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
ratio_ancho = 0.5
ratio_alto = 0.5
im = cv2.resize(im,(0,0),im,ratio_ancho,ratio_alto)
im = cv2.flip(im,0)
cv2.imwrite('reverseDog.png',im)
print('New size: ',im.shape)

root = tk.Tk()
imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(im))
tk.Label(root, image=imgSmaller).pack()

root.mainloop()