import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen = cv2.imread('sudoku.jpg',0)
sobelx = cv2.Sobel(imagen,cv2.CV_64F,0,1,ksize=3)
sobely = cv2.Sobel(imagen,cv2.CV_64F,1,0,ksize=3)

#imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(sobelx))
#im2 = ImageTk.PhotoImage(image=Image.fromarray(imagen))

im3 = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(im3))

laplacia = cv2.Laplacian(imagen,cv2.CV_64F)
im2 = ImageTk.PhotoImage(image=Image.fromarray(laplacia))

tk.Label(root, image=imgSmaller).pack()
tk.Label(root, image=im2).pack()

root.mainloop()
