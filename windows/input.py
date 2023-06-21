from tkinter import *

window = Tk()

## input
entry = Entry(window,
            width=30, fg="green", bg="white",
            font=("Arial", 24, "bold"))
entry.insert(0, "default text")
entry.pack()

## password
pwEntry = Entry(window, width=30, fg="red", bg="white",
            font=("Arial", 24, "bold"), show="*")
pwEntry.insert(0, "****")
pwEntry.pack()

## check button
x = IntVar() # 0 or 1
checkButton = Checkbutton(window, text="Check me", variable=x, onvalue=1, offvalue=0,
                command=lambda: print(x.get()))
checkButton.pack()

## radio button
y = StringVar() # "on" or "off"
radioButton1 = Radiobutton(window, text="On", variable=y, value="on",
                command=lambda: print(y.get()))
radioButton1.pack()
radioButton2 = Radiobutton(window, text="Off", variable=y, value="off",
                command=lambda: print(y.get()))
radioButton2.pack()

z = IntVar() # "on" or "off"
foods = ["Pizza", "Burger", "Pasta"]
for ind in range(len(foods)):
    radioButton = Radiobutton(window, text=foods[ind], variable=z, value=ind,
                command=lambda: print(z.get()))
    radioButton.pack()

## buttons
submit = Button(window, text="Submit", command=lambda: print(entry.get()))
submit.pack(side=BOTTOM)

delete = Button(window, text="Delete", command=lambda: entry.delete(first=0, last=END))
delete.pack(side=RIGHT)

backspace = Button(window, text="Backspace", command=lambda: entry.delete(len(entry.get())-1, END))
backspace.pack(side=LEFT)

window.mainloop()