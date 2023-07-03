from tkinter import *

def keyPress(event):
    print("Key pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.geometry("300x200")
window.bind("<Key>", keyPress)

label = Label(window, text="Press any key", font=("Arial", 20))
label.pack()

window.mainloop()