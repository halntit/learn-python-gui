from tkinter import *

window = Tk()

canvas = Canvas(window, width=200, height=200)

canvas.create_text(100, 100, text="Hello     there!", font=("Times", 20), fill="orange")
canvas.create_line(0, 0, 100, 100, fill="red", width=2)
canvas.create_line(0, 200, 100, 100, fill="green", width=3)
canvas.create_line(100, 100, 200, 0, fill="blue", width=4)
yellowLine = canvas.create_line(100, 100, 200, 200, fill="yellow", width=5)
retangle = canvas.create_rectangle(120, 130, 180, 160, fill="purple")

canvas.pack()

window.mainloop()