import tkinter

window = tkinter.Tk()

stringVar = tkinter.StringVar();
lbl = tkinter.Label(window, textvariable=stringVar)
stringVar.set("Awesome label text")
lbl.pack()

window.mainloop()