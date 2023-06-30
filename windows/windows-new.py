from tkinter import *

def clicked():
    new_window = Toplevel() # create a new window 'on top' of the current window
    new_window.geometry("120x50")
    Button(new_window, text="Close main", command=window.destroy).pack()

def new_clicked():
    new_window = Tk() # create a new window 'on top' of the current window
    new_window.geometry("120x120")
    window.destroy()

window = Tk()
window.geometry("300x200")
Button(window, text="Popup", command=clicked).pack()
Button(window, text="New window", command=new_clicked).pack()
window.mainloop()