import tkinter
from tkinter import messagebox

window = tkinter.Tk()

def popupFunction():
    msg = messagebox.showinfo("Popup Title", "Message")

buttonWidget = tkinter.Button(window, text="Click Me", command=popupFunction)
buttonWidget.place(x=25, y=25)


window.mainloop()