from tkinter import *
import tkinter.messagebox as m

def tempera():

    m.showinfo("Temperatura ",message="La temperatura cambio: "+str(temp.get()))

tk = Tk()
tk.geometry("400x400+500-200")

barraC = Scale(tk,label="Temperatura °C",orient=HORIZONTAL,length=150,from_=-15,to=50,bg="red",fg="dark gray")
barraC.place(x=10,y=20)

temp = DoubleVar()

barraF = Scale(tk,label="Temperatura °F",orient=VERTICAL,length=400,from_=-15,tickinterval=10, variable=temp)
barraF.place(x=100,y=100)

btn = Button(text="Aprieta",command=tempera)

btn.place(x=20,y=200)


tk.mainloop()

