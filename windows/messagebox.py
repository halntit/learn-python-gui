from tkinter import *
from tkinter import messagebox

window = Tk()
def button_clicked():
    messagebox.showinfo(title="Message", message="I got clicked")

def button1_clicked():
    messagebox.showwarning(title="Message", message="I got clicked")

def button2_clicked():
    messagebox.showerror(title="Message", message="Something went wrong")

def button3_clicked():
    # messagebox.askquestion(title="Message", message="Are you sure?") # return "yes" or "no" (string)
    # messagebox.askretrycancel(title="Message", message="Are you want to retry?") # return boolean
    # messagebox.askyesno(title="Message", message="Are you sure?") # return boolean
    # messagebox.askyesnocancel(title="Message", message="Are you sure?")  # return boolean or None
    if messagebox.askokcancel(title="Message", message="Are you sure?", icon=messagebox.WARNING): # return boolean
        print("OK, you are so sure")
    else:
        print("No, you are not sure")

button = Button(window, text="Info window", command=button_clicked)
button.pack()
button1 = Button(window, text="Warning window", command=button1_clicked)
button1.pack()
button2 = Button(window, text="Error window", command=button2_clicked)
button2.pack()
button3 = Button(window, text="Ask window", command=button3_clicked)
button3.pack()

window.mainloop()