from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("300x200")

def open_file():
    filename = filedialog.askopenfilename(
        initialdir="~/Documents", title="Select file",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        defaultextension=".txt"
    )
    file = open(filename, "r")
    if file is None:
        return

    print(file.read())
    file.close()

def clicked():
    input = text.get(1.0, END)
    print(input)

text = Text(window, width=30, height=5, padx=10, pady=10, font=("Times", 18))
text.pack()

button = Button(window, text="Click me", command=clicked)
button.pack()

button = Button(window, text="Open file", command=open_file)
button.pack()

window.mainloop()