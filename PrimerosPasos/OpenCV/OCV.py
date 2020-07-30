import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk

imagen = cv2.imread('perro.jpg')

print("Type: ",type(imagen))
print("Shape: ",imagen.shape)


img = cv2.imread('perroSm.jpg')

#Rearrang the color channel

# A root window for displaying objects
root = tk.Tk()

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgCv = ImageTk.PhotoImage(image=im)

b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))
im = Image.fromarray(img)
imgOri = ImageTk.PhotoImage(image=im)

imgBW = ImageTk.PhotoImage(image=Image.fromarray(cv2.imread("perroSm.jpg",cv2.IMREAD_GRAYSCALE)))

# Put it in the display window

tk.Label(root, image=imgCv).pack()
tk.Label(root, image=imgOri).pack()
tk.Label(root, image=imgBW).pack()

root.mainloop() # Start the GUI