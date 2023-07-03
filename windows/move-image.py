from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("Move Image")

# Create a canvas
canvas = Canvas(window, width=500, height=500, bg="green")
canvas.pack()

# Create an image
img = PhotoImage(file="windows/icon.png")
image = canvas.create_image(0, 0, anchor=NW, image=img)

def moveUp(event):
    canvas.move(image, 0, -10)
def moveDown(event):
    canvas.place(x=canvas.winfo_x(), y=canvas.winfo_y() + 10)
def moveLeft(event):
    canvas.place(x=canvas.winfo_x() - 10, y=canvas.winfo_y())
def moveRight(event):
    canvas.place(x=canvas.winfo_x() + 10, y=canvas.winfo_y())

window.bind("<w>", moveUp)
window.bind("<Up>", moveUp)
window.bind("<s>", moveDown)
window.bind("<a>", moveLeft)
window.bind("<d>", moveRight)

# # Bind mouse events to the canvas
# def dragStart(event):
#     widget = event.widget # tmp reference to the widget
#     widget.startX = event.x
#     widget.startY = event.y

# def dragMotion(event):
#     widget = event.widget # tmp reference to the widget
#     x = widget.winfo_x() - widget.startX + event.x
#     y = widget.winfo_y() - widget.startY + event.y
#     widget.place(x=x, y=y)

# canvas.bind("<Button-1>", dragStart)
# canvas.bind("<B1-Motion>", dragMotion)

window.mainloop()
