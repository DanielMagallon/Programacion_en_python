import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

imagen1 = cv2.imread('perroSm.jpg')
watermark = cv2.imread("marca-agua-redaitcurso.jpg")

imagen1 = cv2.cvtColor(imagen1,cv2.COLOR_BGR2RGB)
watermark = cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)

imagen1 = cv2.resize(imagen1,(800,800))
watermark = cv2.resize(watermark,(800,800))

mixed_img = cv2.addWeighted(src1=imagen1,alpha=0.5,src2=watermark,beta=0.5,gamma=0)

imgSmaller = ImageTk.PhotoImage(image=Image.fromarray(mixed_img))

tk.Label(root, image=imgSmaller).pack()

root.mainloop()
