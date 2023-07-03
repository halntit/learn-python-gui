from tkinter import *
import time

W = 500
H = 500
xV = 3 # velocity
yV = 2

window = Tk()
window.geometry(f"{W}x{H}")
window.title("Animation")

canvas = Canvas(window, width=W, height=H)
canvas.pack()

image = PhotoImage(file="windows/icon.png")
icon = canvas.create_image(0, 0, anchor=NW, image=image)
iconW = image.width()
iconH = image.height()

while True:
    coordinates = canvas.coords(icon)
    if (coordinates[0] > (W-iconW) or coordinates[0] < 0):
        xV = -xV
    if (coordinates[1] > H-iconH or coordinates[1] < 0):
        yV = -yV
    canvas.move(icon, xV, yV)
    window.update()
    time.sleep(0.01)

window.mainloop()