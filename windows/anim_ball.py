class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color) -> None:
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        self.canvas.move(self.image, self.xVelocity, self.yVelocity)
        coords = self.canvas.coords(self.image)
        if coords[0] <= 0 or coords[2] >= self.canvas.winfo_width():
            self.xVelocity = -self.xVelocity
        if coords[1] <= 0 or coords[3] >= self.canvas.winfo_height():
            self.yVelocity = -self.yVelocity
