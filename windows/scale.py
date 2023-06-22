from tkinter import *

window = Tk()
window.title("Scale")

scale = Scale(window, from_=0, to=100, orient=VERTICAL,
            length=200,
            tickinterval=10, # default: 1 (show every 10)
            resolution=5, # default: 1 increment of slider
            # showvalue=0, # default: 1 (show value on slider)
            troughcolor="#69eaff", # default: "grey"
)
scale.set(50) # default: 0
scale.pack()

button = Button(window, text="Click me", command=lambda: print(scale.get()))
button.pack()

window.mainloop()