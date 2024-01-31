from tkinter import * 
from PIL import ImageTk, Image

fenetre=Tk()

menubar=Menu(fenetre)
f1=Menu(menubar,tearoff=0)
f2=Menu(menubar,tearoff=0)
f1.add_command(label='New')
f1.add_separator()
f1.add_command(label='Open')
f1.add_separator()
f1.add_command(label='Exit',command=fenetre.destroy)
f2.add_command(label='cours')
f2.add_separator()
f2.add_command(label='Tds')
menubar.add_cascade(label='File',menu=f1)
menubar.add_cascade(label='Options',menu=f2)
fenetre.config(menu=menubar)




fenetre.mainloop()