from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=200)
canvas.create_arc(0, 0, 200, 200, fill="red", extent=180, width=10)
canvas.create_arc(0, 0, 200, 200, fill="white", extent=180, start=180, width=10)
canvas.create_oval(80, 80, 120, 120, fill="white", width=10)
canvas.pack()

window.mainloop()