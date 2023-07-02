from tkinter import *
## grid() = geometry manager that organizes widgets in a table-like structure

window = Tk()

firstNameLabel = Label(window, text="First Name").grid(row=0, column=0, sticky=E)
firstNameEntry = Entry(window).grid(row=0, column=1)
lastNameLabel = Label(window, text="Last Name").grid(row=1, column=0, sticky=E)
lastNameEntry = Entry(window).grid(row=1, column=1)
emailLabel = Label(window, text="Email").grid(row=2, column=0, sticky=E) # sticky = align
emailEntry = Entry(window).grid(row=2, column=1)
addressLabel = Label(window, text="Address").grid(row=3, column=0, sticky=E)
addressEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2, sticky=W+E+N+S)

window.mainloop()
