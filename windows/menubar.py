from tkinter import *
from tkinter import filedialog

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

def save():
    file = filedialog.asksaveasfile(
        initialdir="~/Documents", title="Save to",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        defaultextension=".txt"
    )
    input = str(text.get(1.0, END))
    file.write(input)
    file.close()

window = Tk()
window.geometry("300x200")

menu = Menu(window)
window.config(menu=menu)

fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

editMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", image=PhotoImage(file="windows/undo.png"), compound=LEFT)
editMenu.add_command(label="Redo")

text = Text(window, width=30, height=5, padx=10, pady=10, font=("Times", 18))
text.pack()

window.mainloop()