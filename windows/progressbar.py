from tkinter import *
from tkinter.ttk import *
import time

window = Tk()

def start():
    tasks = 50
    curr = 0
    while (curr < tasks):
        curr += 1
        bar['value'] = curr*100/tasks
        time.sleep(0.05)
        percent.set(str(curr*100/tasks))
        task.set(str(curr) + "/" + str(tasks))
        window.update_idletasks() # update the progress bar (without this, the progress bar will not updated)

percent = StringVar()
task = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=200)
bar.pack()
percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=task).pack()

button = Button(window, text="Click me", command=start).pack()

window.mainloop()