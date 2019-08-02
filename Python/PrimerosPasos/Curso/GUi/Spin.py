from tkinter import *

tk = Tk()

tk.geometry("300x300+0+0")

spn = Spinbox(tk,values=[100,90,80,70,"Reprobado"])
spn.place(x=0,y=0)

spn2 = Spinbox(tk,from_=70,to=100)
spn2.place(x=30,y=50)

tk.mainloop()