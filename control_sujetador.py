from asyncio.windows_events import NULL
from tkinter import *

window = Tk()
window.title('Control Manual')

#value initialization
def init():
    t1.delete("1.0", END)
    t1.insert(END,0.000)
    t2.delete("1.0", END)
    t2.insert(END,0.000)
    t3.delete("1.0", END)
    t3.insert(END,0.000)
    t4.delete("1.0", END)
    t4.insert(END,0.000)

#apply button
def apply():
    x_pos = x_value.get()
    y_pos = y_value.get()
    z_pos = z_value.get()
    r_pos = r_value.get()

    if x_pos != "":
        x_pos = float(x_pos)
    if y_pos != "":
        y_pos = float(y_pos)
    if z_pos != "":
        z_pos = float(z_pos)
    if r_pos != "":
        r_pos = float(r_pos)
 
   
    t1.delete("1.0", END)
    t1.insert(END,x_pos)
    t2.delete("1.0", END)
    t2.insert(END,y_pos)
    t3.delete("1.0", END)
    t3.insert(END,z_pos)
    t4.delete("1.0", END)
    t4.insert(END,r_pos)

#x_pos = 0.00
#y_pos = 0.00
#z_pos = 0.00
#r_pos = 0.00


x_value = StringVar()
y_value = StringVar()
z_value = StringVar()
r_value = StringVar()

#text entries
e1 = Entry(window, textvariable=x_value)
e2 = Entry(window, textvariable=y_value)
e3 = Entry(window, textvariable=z_value)
e4 = Entry(window, textvariable=r_value)

#text labels
e5 = Label(window, text="X")
e6 = Label(window, text="Y")
e7 = Label(window, text="Z")
e8 = Label(window, text="r")
e9 = Label(window, text="Ingrese valores +/-")
e10 = Label(window, text="Valor actual")

#text outputs
t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)
t4 = Text(window, height=1, width=20)

#buttons
b1 = Button(window, text = "Aplicar", command=apply)
b2 = Button(window, text = "Parar")

#grid placement
e1.grid(row=1,column=0)
e2.grid(row=2,column=0)
e3.grid(row=3,column=0)
e4.grid(row=4,column=0)
b2.grid(row=5,column=0)
e5.grid(row=1,column=1)
e6.grid(row=2,column=1)
e7.grid(row=3,column=1)
e8.grid(row=4,column=1)
e9.grid(row=0,column=0)
e10.grid(row=0,column=2)
t1.grid(row=1,column=2)
t2.grid(row=2,column=2)
t3.grid(row=3,column=2)
t4.grid(row=4,column=2)
b1.grid(row=5,column=2)

init()

window.mainloop()