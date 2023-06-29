from tkinter import *
from tkinter import filedialog

window = Tk()
window.geometry("300x200")

def save():
    file = filedialog.asksaveasfile(
        initialdir="~/Documents", title="Save to",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        defaultextension=".txt"
    )
    input = str(text.get(1.0, END))
    file.write(input)
    file.close()

text = Text(window, width=30, height=5, padx=10, pady=10, font=("Times", 18))
text.pack()

button = Button(window, text="Save file", command=save)
button.pack()

window.mainloop()