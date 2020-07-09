import tkinter as tk

class App:

    def __init__(self):
        self.wind = tk.Tk()
        self.canvas = tk.Canvas(self.wind,width=600,height=400,bg="black")
        self.canvas.bind("<Motion>",self.mover_mouse)

        self.canvas.bind("<Button-1>", self.presion_mouse)
        self.canvas.bind("<B1-Motion>", self.dragged_mouse)
        self.canvas.grid(row=0,column=1)
        self.wind.mainloop()

    def presion_mouse(self, evento):
        pass

    def mover_mouse(self, evento):
        self.wind.title(str(evento.x) + "-" + str(evento.y))

    def dragged_mouse(self,evento):
        self.canvas.create_oval(evento.x - 5, evento.y - 5, evento.x + 50, evento.y + 50, fill="red")

App()
