from tkinter import *

window = Tk()
window.geometry("300x200")

frame = Frame(window, relief=SUNKEN, borderwidth=5, padx=10, pady=10, bg="#ccc")
frame.place(x=10, y=10)

Button(frame, text="W", width=2).pack(side=TOP)
Button(frame, text="A", width=2).pack(side=LEFT)
Button(frame, text="S", width=2).pack(side=LEFT)
Button(frame, text="D", width=2).pack(side=LEFT)

window.mainloop()