from tkinter import *
from PIL import Image, ImageTk
import numpy

# simple gui with three canvases
class Gui:
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, height=100, width=100)
        self.canvas.pack()

        self.canvas2 = Canvas(self.root, height=100, width=100)
        self.canvas2.pack()

        self.canvas3 = Canvas(self.root, height=100, width=100)
        self.canvas3.pack()

    def start(self):
        self.root.mainloop()

    def setNumpyImage(self, numImg):
        self.img = ImageTk.PhotoImage(image=Image.fromarray(numImg))
        self.canvas2.create_image(0, 0, anchor="nw", image=self.img)

    def setPhotoImage(self, photoImage):
        self.canvas3.create_image(0, 0, anchor="nw", image=photoImage)

gui = Gui()

numpyImg = numpy.random.randint(low=0,high=255,size=(100,100,3),dtype='uint8')

#setting image directly
photoImg = ImageTk.PhotoImage(image=Image.fromarray(numpyImg))
gui.canvas.create_image(0, 0, anchor="nw", image=photoImg)

#setting image via function
gui.setNumpyImage(numpyImg)

#setting photoImage
gui.setPhotoImage(photoImg)

gui.start()