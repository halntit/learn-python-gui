from tkinter import *

def mouseMove(event):
    label.config(text=str(event.x) + ", " + str(event.y))

def mousePress(event):
    label.config(text="Mouse pressed at " + str(event.x) + ", " + str(event.y))

window = Tk()
window.geometry("300x200")
window.bind("<Motion>", mouseMove)
window.bind("<Button-1>", mousePress)

label = Label(window, text="Press any key", font=("Arial", 20))
label.pack()

window.mainloop()