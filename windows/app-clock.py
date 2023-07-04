from tkinter import *
from time import *

def tick():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    date_string = strftime("%A %d %B %Y")
    date_label.config(text=date_string)

    time_label.after(1000, tick)

window = Tk()

time_label = Label(window, text="Time")
time_label.pack()

date_label = Label(window, text="Date")
date_label.pack()

tick()

window.mainloop()