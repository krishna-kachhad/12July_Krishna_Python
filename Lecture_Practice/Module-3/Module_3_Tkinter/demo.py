import tkinter
from tkinter import ttk
from tkinter import messagebox

m=tkinter.Tk()
m.geometry("400x500")
m.config(background='orange')
#tkinter.Label(text="Firstname").pack()

'''lblfnm=tkinter.Label(text="Firstname")
lblfnm.pack()

lbllnm=tkinter.Label(text="Lastname")
lbllnm.pack()'''

'''lblfnm=tkinter.Label(text="Firstname")
lblfnm.place(x=0,y=0)

lbllnm=tkinter.Label(text="Lastname")
lbllnm.place(x=0,y=30)'''

lblfnm=tkinter.Label(text="Firstname:",bg="orange",fg='green',font='Bahnschrift 15 bold')
lblfnm.grid(row=0,column=0,sticky='W')

lbllnm=tkinter.Label(text="Lastname:",bg="orange",fg='green',font='Bahnschrift 15 bold')
lbllnm.grid(row=1,column=0,sticky='W')

txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')

txtlnm=tkinter.Entry()
txtlnm.grid(row=1,column=1,sticky='W')

male=tkinter.Radiobutton(value=0, text="Male",bg="orange",fg='green',font='Bahnschrift 15 bold')
male.grid(row=2,column=0,sticky='W')

female=tkinter.Radiobutton(value=1,text="Female",bg="orange",fg='green',font='Bahnschrift 15 bold')
female.grid(row=2,column=1,sticky='W')

guj=tkinter.Checkbutton(text="Gujarti",bg="orange",fg='green',font='Bahnschrift 15 bold')
guj.grid(row=3,column=0,sticky='W')

hin=tkinter.Checkbutton(text="Hindi",bg="orange",fg='green',font='Bahnschrift 15 bold')
hin.grid(row=4,column=0,sticky='W')

eng=tkinter.Checkbutton(text="English",bg="orange",fg='green',font='Bahnschrift 15 bold')
eng.grid(row=5,column=0,sticky='W')

city=['Rajkot','Ahmedabad','Surat','Baroda','Jamnagar','Junagadh']
ctcombo=ttk.Combobox(values=city)
ctcombo.grid(row=6,column=0)


def btnclick():
    messagebox.askquestion("Confirm","Are you sure?") 

btn=tkinter.Button(command=btnclick,text="Submit",font='Bahnschrift 15 bold')
btn.place(x=160,y=250)


m.mainloop()