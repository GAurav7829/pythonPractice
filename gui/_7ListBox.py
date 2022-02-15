from msilib.schema import ListBox
import tkinter

window = tkinter.Tk()

lBox = tkinter.Listbox(window)
lBox.insert(1, "Item 1")
lBox.insert(2, "Item 2")
lBox.insert(3, "Item 3")
lBox.pack()

window.mainloop()