from tkinter import *
from tkinter import ttk

def button_clicked(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
    except:
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.geometry("500x500")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, bg="white", font=("Arial", 20, "bold"), width=26, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, command=lambda:button_clicked('1'))
button1.grid(row=0, column=0)
button2 = Button(frame, text=2, height=4, width=9, command=lambda:button_clicked('2'))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, command=lambda:button_clicked('3'))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, command=lambda:button_clicked('4'))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, command=lambda:button_clicked('5'))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, command=lambda:button_clicked('6'))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, command=lambda:button_clicked('7'))
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, command=lambda:button_clicked('8'))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, command=lambda:button_clicked('9'))
button9.grid(row=2, column=2)

button_plus = Button(frame, text='+', height=4, width=9, command=lambda:button_clicked('+'))
button_plus.grid(row=0, column=3)
button_minus = Button(frame, text='-', height=4, width=9, command=lambda:button_clicked('-'))
button_minus.grid(row=1, column=3)
button_multiply = Button(frame, text='*', height=4, width=9, command=lambda:button_clicked('*'))
button_multiply.grid(row=2, column=3)
button_devide = Button(frame, text='/', height=4, width=9, command=lambda:button_clicked('/'))
button_devide.grid(row=3, column=3)

button0 = Button(frame, text=0, height=4, width=9, command=lambda:button_clicked('0'))
button0.grid(row=3, column=0)
button_decimal = Button(frame, text='.', height=4, width=9, command=lambda:button_clicked('.'))
button_decimal.grid(row=3, column=1)
button_equal = Button(frame, text='=', height=4, width=9, command=lambda:equals())
button_equal.grid(row=3, column=2)

button_clear = Button(window, text='Clear', height=4, width=30, command=lambda:clear()).pack()

window.mainloop()