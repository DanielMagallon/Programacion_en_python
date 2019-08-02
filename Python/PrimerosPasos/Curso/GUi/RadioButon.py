from tkinter import *
from tkinter import messagebox as ms

cads = ["Bien", "Excelente", "Aburrido"]


def estado():
    valor = varGrupo.get()
    ms.showinfo("Estado de animo", "Hoy te sientes %s" % cads[valor])

def lenguajes():
    lgs=""
    i=0
    for vc in varChecks:
        if vc.get()==1: lgs+=" "+cad2[i]
        i+=1
    ms.showinfo("Usted conoceid",lgs)



rds = []

s = Tk()
s.geometry("300x200+10+10")

varGrupo = IntVar()
y = 10
x = 0
for i in range(len(cads)):
    rds.insert(i, Radiobutton(s, text=cads[i], value=i, variable=varGrupo, command=estado))
    rds[i].place(x=x, y=y)
    x += 15
    y += 20

checks = []

cad2 = ["Java", "Python", "C++", "PHP", "Visual Basic"]

varChecks = []

for i in range(len(cad2)):
    varChecks.insert(i,IntVar())
    checks.insert(i, Checkbutton(s, text=cad2[i], variable=varChecks[i], onvalue=1, offvalue=0,command=lenguajes))
    checks[i].place(x=x, y=y)
    x += 15
    y += 20

# rdbBien = Radiobutton(s,text=cads[0],value=0,variable=varGrupo,command=estado)
# rbdExcelnte = Radiobutton(s,text=cads[1],value=1,variable=varGrupo,command=estado)
# rbdBored = Radiobutton(s,text=cads[2],value=2,variable=varGrupo,command=estado)

# rdbBien.place(x=0,y=10)
# rbdExcelnte.place(x=15,y=30)
# rbdBored.place(x=30,y=50)
s.mainloop()
