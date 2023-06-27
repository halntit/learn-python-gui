from tkinter import *
import os

def add():
    listBox.insert(END, entry.get())
    entry.delete(0, END)
    listBox.config(height=listBox.size())

def delete():
    for i in reversed(listBox.curselection()):
        listBox.delete(i)
    # selected = list(map(int, listBox.curselection()))
    # for i in reversed(selected):
    #     listBox.delete(i)
    listBox.config(height=listBox.size())

def submit():
    selected = list(map(int, listBox.curselection()))
    for i in selected:
        print (listBox.get(i))

window = Tk()

listBox = Listbox(window,
    background="#f7ffde", selectbackground="#ccc",
    width=50, selectmode=MULTIPLE)
listBox.insert(1, "First entry")
listBox.insert(2, "Second entry")
listBox.insert(3, "Third entry")
listBox.insert(4, "Fourth entry")

listBox.config(height=listBox.size())
listBox.pack()

entry = Entry(window, width=50)
entry.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

delButton = Button(window, text="Delete", command=delete)
delButton.pack()

button = Button(window, text="Click me", command=submit)
button.pack()

window.mainloop()