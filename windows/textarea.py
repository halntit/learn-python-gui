from tkinter import *

window = Tk()
window.geometry("300x200")

def clicked():
    input = text.get(1.0, END)
    print(input)

text = Text(window, width=30, height=5, padx=10, pady=10, font=("Times", 18))
text.pack()

button = Button(window, text="Click me", command=clicked)
button.pack()

window.mainloop()