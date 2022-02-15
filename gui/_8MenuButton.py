from msilib.schema import ListBox
import tkinter

window = tkinter.Tk()

mButton = tkinter.Menubutton(window, text="Click Me")
mButton.grid()
mButton.menu = tkinter.Menu(mButton)
mButton["menu"] = mButton.menu

mButton.menu.add_checkbutton(label="Item 1")
mButton.menu.add_checkbutton(label="Item 2")
mButton.menu.add_checkbutton(label="Item 3")

mButton.pack()

window.mainloop()