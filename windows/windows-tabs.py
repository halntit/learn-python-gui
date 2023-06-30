from tkinter import *
from tkinter import ttk # themed tkinter

window = Tk()
window.geometry("300x200")

notebook = ttk.Notebook(window) # widget manages the tabs
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill=BOTH) # BOTH or X or Y

Label(tab1, text="Tab 1").pack()
Label(tab2, text="Tab 2").pack()

window.mainloop()