from tkinter import *


tk = Tk()
tk.geometry("400x400+500-200")
tk.iconbitmap(bitmap="/home/yeo/Descargas/img.xbm")
#no se puede usar el place aqui, y luego insertar
#listab = Listbox(tk).place(x=100,y=20)
listab = Listbox(tk)
listab.place(x=100,y=20)

lenguajes = ["Java","Python","C++","C#","PHP","Javascript"]

for leng in lenguajes:
    listab.insert(END,leng)

#listab.delete(0,2)

tk.mainloop()