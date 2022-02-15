import tkinter
window = tkinter.Tk()

frame = tkinter.Frame(window)
frame.pack()

btn = tkinter.Button(frame, text="Hello")
btn.pack(side=tkinter.LEFT)

cv = tkinter.IntVar()
cb = tkinter.Checkbutton(frame, text="Text", variable=cv, onvalue=1, offvalue=0, height=5, width=20)
cb.pack()

window.mainloop()