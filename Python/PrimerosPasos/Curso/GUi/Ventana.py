from tkinter import *

#ventana = Frame(height=400,width=300,cursor="cross")
#Margen en x y margen y para cada compente que se agregue
#ventana.pack(padx=10,pady=20)

#ventana.mainloop()


tk = Tk()
#Ancho y alto,pos en x & y
#tk.geometry("400x400+100+100")
tk.title("Aplicacion Visual")
#Solo en widnows es necesario poner tk.mainloop, segun
#lblUser = Label(text="Usuario:").place(x=10,y=50)
#lbl2 = Label(text="Yeo").place(x=100,y=50)

#grid::  sticky: W pa la derecha, E para la izquierda
lblConGrid = Label(text="Label con grid",fg="blue",bg="orange").grid(row=0,column=0)
lblGrid2 = Label(text="Label grid 2",fg="red",bg="black")

lblGrid2.grid(row=0,column=1)

#con grid no es necesario usar el geometry

#Si usamos el place ya no es ncesario el pack, o marcara error
#lbl2.pack()
#lblUser.pack()
tk.mainloop()
