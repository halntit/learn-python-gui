from tkinter import *
import os

## Widgets: GUI elements: buttons, labels, text boxes, etc.
## Windows: Serve as containers to hold and organize widgets
## Labels: Display text and images
## Buttons: Trigger actions when clicked on them

# Create a window
window = Tk()

# Add title, icon, size, background color
window.geometry("420x500")
window.title("My First GUI Program")
window.config(padx=20, pady=20, background="#ccc")
# ----------------------------------------------
thisdir = os.path.dirname(__file__)
icon = os.path.join(thisdir, 'icon.png')
window.iconphoto(True, PhotoImage(file=icon))

# Add label
label = Label(window, text="I am a label", font=("Arial", 24, "bold"), 
    relief="solid", bg="white", fg="black", padx=20, pady=20)
label.pack() # Add label to window
label2 = Label(window, text="xXx", font=("Arial", 12), bg="blue", fg="white")
label2.place(x=0, y=0)
label3 = Label(window, text="yYy", font=("Arial", 12), bg="red", fg="white")
# place to the right edge of window
# label3.place(x=window.winfo_width()-label3.winfo_width(), y=0)
label3.place(x=350, y=0)

# Add photo
photo_label = Label(window, text="I am a photo label", 
    image=PhotoImage(file=icon), compound="bottom")
photo_label.pack()

# Add button
def button_clicked():
    label.config(text="I got clicked")

button = Button(window, text="Click Me", command=button_clicked,
    font=("Comic Sans MS", 24, "bold"), activebackground="red",
     state=NORMAL, compound="top")
button.pack()

window.mainloop() # Keep the window on screen