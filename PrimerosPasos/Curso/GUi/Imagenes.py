from tkinter import *




tk = Tk()
tk.geometry("400x400+500-200")
tk.config(bg="#FFFFAA")

tierra = PhotoImage(file="tierra.gif")
luna = PhotoImage(file="luna.gif")

lbl=Label(tk,image=tierra).place(x=0,y=0)
lblLuna = Button(tk,image=luna).place(x=500,y=200)



tk.mainloop()
