import cv2
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

root = tk.Tk()

imagen = cv2.imread('perroSm.jpg')
imagen2 = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
histo = cv2.calcHist([imagen2],[0],None,[256],[0,256])

print("Histogram: ",plt.plot(histo))

imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(histo),size=(400,400))

colores = ('b','g','r')
for i,color in enumerate(colores):
    histo = cv2.calcHist([imagen2],[i],None,[256],[0,256])
    plt.plot(histo)
    plt.xlim([0,256])


tk.Label(root, image=imgSmaller,width=400,height=400).pack()

root.mainloop()
