from tkinter import *
import tkinter.messagebox as m

def close():
    m.showinfo("Saliendo...","Programa finalizado")
    tk.destroy()
    pass

tk = Tk()
tk.geometry("400x400+500-200")
barramenu = Menu(tk)
menuArchivo = Menu(barramenu)
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_separator()
menuArchivo.add_command(label="Cerrar",command=close)

var = IntVar()

barramenu.add_cascade(label="Archivo",menu=menuArchivo)
tk.config(menu=barramenu)


tk.mainloop()
