import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

file = None

def change_color():
    color = colorchooser.askcolor(title="Change color")
    if color:
        colorHex = color[1]
        text_area.config(fg=colorHex)

def change_font(*args):
    text_area.configure(font=(font_name.get(), font_size.get()))

def new_file():
    window.title("Untitled")
    text_area.delete("1.0", END)

def open_file():
    filename = filedialog.askopenfilename(
        initialdir="~/Documents", title="Select file",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        defaultextension=".txt"
    )
    file = open(filename, "r")
    if file is None:
        return

    window.title(os.path.basename(filename))
    text_area.delete("1.0", END)
    text_area.insert("1.0", file.read())
    file.close()

def save_file():
    filename = filedialog.asksaveasfilename(
        initialdir="~/Documents", title="Save to",
        filetypes=(("text files", "*.txt"), ("all files", "*.*")),
        defaultextension=".txt"
    )
    file = open(filename, "w")
    if file is None:
        return
    file.write(text_area.get("1.0", END))
    file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About", "This is a text editor", icon="info")

def quit():
    window.destroy()


window_w = 500
window_h = 500
window = Tk()
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

x = int(screen_w/2 - window_w/2)
y = int(screen_h/2 - window_h/2)

window.title("Text Editor")
window.geometry("{}x{}+{}+{}".format(window_w, window_h, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = IntVar(window)
font_size.set(24)

text_area = Text(window, font=(font_name.get(), font_size.get()))
scrollbar = Scrollbar(text_area)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N+S+E+W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="Change color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, textvariable=font_size, from_=8, to=72, increment=1, command=change_font)
size_box.grid(row=0, column=2)

scrollbar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrollbar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()