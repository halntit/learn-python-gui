from tkinter import *

def dragStart(event):
    widget = event.widget # tmp reference to the widget
    widget.startX = event.x
    widget.startY = event.y

def dragMotion(event):
    widget = event.widget # tmp reference to the widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, text="Drag 2!", font=("Arial", 20), bg="yellow")
label.place(x=0, y=0)
label.bind("<Button-1>", dragStart)
label.bind("<B1-Motion>", dragMotion)

label2 = Label(window, text="Drag 1!", font=("Tahoma", 20), bg="green")
label2.place(x=10, y=20)
label2.bind("<Button-1>", dragStart)
label2.bind("<B1-Motion>", dragMotion)

window.mainloop()