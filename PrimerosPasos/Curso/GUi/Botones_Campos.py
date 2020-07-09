from tkinter import *
from tkinter import messagebox

def sumar():
    n = int(entrada.get())
    n2 = int(entrada2.get())
    messagebox.showinfo("Suma de los numeros",f"La suma es: {n+n2}",type="ok",icon=messagebox.INFO)
    entrada2.set("")
    entrada.set("")
    



tk = Tk()
tk.geometry("400x400+500-200")
tk.title("Ventana con funciones")

lbl = Label(text="Escriba un numero: ",font=("Ani",18)).place(x=10,y=10)
entrada = StringVar()
entrada.set(10)
txt = Entry(tk,textvariable=entrada).place(x=200,y=20)

lbl2 = Label(text="Escriba otro numero: ",font=("Ani",18)).place(x=10,y=100)
entrada2 = StringVar()
entrada2.set(20)
txt2 = Entry(tk,textvariable=entrada2,width="10").place(x=220,y=110)

btnSumar = Button(tk,text='Sumar',font=("Abyssinica SIL",27),fg="red",activeforeground="blue",
                  activebackground="purple",command = sumar)



btnSumar.place(x=150,y=170)

tk.mainloop()