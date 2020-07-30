import cv2
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageTk

root = tk.Tk()

imagen = cv2.imread('perroSm.jpg',0)

figura = plt.figure(figsize=(100,100))
lienzo = figura.add_subplot(111)

im_plt = lienzo.imshow(imagen)

image1 = Image.fromarray(np.uint8( im_plt.get_cmap()(im_plt.get_array())*255))
im = ImageTk.PhotoImage('RGB', image1.size)

tk.Label(root, image=im).pack()

root.mainloop()