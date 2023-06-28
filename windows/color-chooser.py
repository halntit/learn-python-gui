from tkinter import *
from tkinter import colorchooser

window = Tk()
window.geometry("300x200")
window.title("Color Chooser")

def clicked():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)

button = Button(window, text="Click me", command=clicked)
button.pack()

window.mainloop()