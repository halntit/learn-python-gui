from tkinter import *
import time
from anim_ball import *

W = 500
H = 500
xV = 3 # velocity
yV = 2

window = Tk()
window.geometry(f"{W}x{H}")
window.title("Animation")

canvas = Canvas(window, width=W, height=H)
canvas.pack()

volley_ball = Ball(canvas, x=2, y=3, diameter=50, xVelocity=xV, yVelocity=yV, color="red")
foot_ball = Ball(canvas, 4, 5, 20, 1, 2, "green")
basket_ball = Ball(canvas, 10, 12, 20, 4, 8, "pink")

while True:
    volley_ball.move()
    foot_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()