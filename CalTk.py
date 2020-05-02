from tkinter import *

root = Tk()
root.title("Calculator")
total = 0
mathType = 1

def numberClick(number):
    inNum = inputNum.get()
    indexLen = len(inNum)
    #str(number)
    inputNum.insert(indexLen, number)
def clearClick():
    inputNum.delete(0, END)
def addClick():
    global total
    current = inputNum.get()
    current = int(current)
    total = current + total
    print(current, total)
    inputNum.delete(0, END)
    mathType = 1
def equalClick():
    global total
    if(mathType == 1):
        total = total + int(inputNum.get())
        inputNum.delete(0, END)
        inputNum.insert(0, total)
        mathType = 0
def clearAllClick():
    global total
    total = 0
    inputNum.delete(0, END)



inputNum = Entry(root, width=30, borderwidth=5)

button2 = Button(root, text="2", padx=40, pady=20, command=lambda: numberClick(2))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: numberClick(1))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: numberClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: numberClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: numberClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: numberClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: numberClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: numberClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: numberClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: numberClick(0))
clearButton = Button(root, text="Clear", padx=29, pady=20, command=clearClick)
addButton = Button(root, text="+", padx=39, pady=20, command=addClick)
equalButton = Button(root, text="=", padx=92, pady=20, command=equalClick)
clearAllButton = Button(root, text="CA", padx=35, pady=20, command=clearAllClick)



inputNum.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
clearButton.grid(row=4, column=1)
addButton.grid(row=4, column=2)
equalButton.grid(row=5, column=1, columnspan=2)
clearAllButton.grid(row=5, column=0)



root.mainloop()