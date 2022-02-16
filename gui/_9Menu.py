import tkinter
from tkinter import messagebox

def popupFunction():
    msg = messagebox.showinfo("Popup Title", "Hello Python")

window = tkinter.Tk()

menubar = tkinter.Menu(window)

menu1 = tkinter.Menu(menubar)
menu1.add_command(label="New")
menu1.add_command(label="Show Hello Python Popup", command=popupFunction)
menu1.add_separator()
menu1.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="Section 1", menu=menu1)

menu2 = tkinter.Menu(menubar)
menu2.add_command(label="Undo")

menubar.add_cascade(label="Section 2", menu=menu2)

window.config(menu=menubar)

window.mainloop()
