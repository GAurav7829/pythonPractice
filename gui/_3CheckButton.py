import tkinter

window = tkinter.Tk()

cv = tkinter.IntVar()
cv = tkinter.Checkbutton(window, text="Text", variable=cv, onvalue=1, offvalue=0, height=40, width=30)
cv.pack()

window.mainloop()