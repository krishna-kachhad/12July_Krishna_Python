import tkinter
from tkinter import ttk
from tkinter import messagebox

m=tkinter.Tk()
m.geometry("400x500")
lblfnm=tkinter.Label(text="Value1:",bg="orange",fg='blue',font='Bahnschrift 15 bold')
lblfnm.grid(row=0,column=0,sticky='W')

lbllnm=tkinter.Label(text="Value2:",bg="orange",fg='blue',font='Bahnschrift 15 bold')
lbllnm.grid(row=1,column=0,sticky='W')

txt1=tkinter.Entry()
txt1.grid(row=0,column=1,sticky='W')

txt2=tkinter.Entry()
txt2.grid(row=1,column=1,sticky='W')

def add():
    v1 = int(txt1.get())
    v2 = int(txt2.get())
    a = v1+v2
    print("Value1:", txt1.get())
    print("Value2:", txt2.get())
    messagebox.showinfo("Your Data", a)

btn=tkinter.Button(command=add, text="Add",font='Bahnschrift 12 bold')
btn.place(x=40,y=80)

def sub():
    v1 = int(txt1.get())
    v2 = int(txt2.get())
    s = v1-v2
    print("Value1:", txt1.get())
    print("Value2:", txt2.get())
    messagebox.showinfo("Your Data", s)

btn=tkinter.Button(command=sub, text="Sub",font='Bahnschrift 12 bold')
btn.place(x=90,y=80)

def mul():
    v1 = int(txt1.get())
    v2 = int(txt2.get())
    m = v1*v2
    print("Value1:", txt1.get())
    print("Value2:", txt2.get())
    messagebox.showinfo("Your Data", m)

btn=tkinter.Button(command=mul, text="Mul",font='Bahnschrift 12 bold')
btn.place(x=140,y=80)

def div():
    v1 = int(txt1.get())
    v2 = int(txt2.get())
    d = v1/v2
    print("Value1:", txt1.get())
    print("Value2:", txt2.get())
    messagebox.showinfo("Your Data", d)

btn=tkinter.Button(command=div, text="Div",font='Bahnschrift 12 bold')
btn.place(x=190,y=80)

m.mainloop()