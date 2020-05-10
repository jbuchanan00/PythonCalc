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
    global mathType
    current = inputNum.get()
    current = int(current)
    total = current + total
    inputNum.delete(0, END)
    mathType = 1
def equalClick():
    global total
    global mathType
    if(mathType == 1):
        total = total + int(inputNum.get())
        inputNum.delete(0, END)
        inputNum.insert(0, total)
    elif(mathType == 2):
        total = total - int(inputNum.get())
        inputNum.delete(0, END)
        inputNum.insert(0, total)
    elif(mathType == 3):
        total = total * int(inputNum.get())
        inputNum.delete(0, END)
        inputNum.insert(0, total)
    elif(mathType == 4):
        total = total / int(inputNum.get())
        inputNum.delete(0, END)
        inputNum.insert(0, total)
    else:
        inputNum.delete(0, END)
        inputNum.insert(0, "Error Occured")
    print(mathType)
    mathType = 0
def clearAllClick():
    global total
    total = 0
    inputNum.delete(0, END)

def subtractClick():
    global mathType
    global total
    mathType = 2
    current = int(inputNum.get())
    total = current - total
    inputNum.delete(0, END)
def multiplyClick():
    global mathType
    global total
    mathType = 3
    current = int(inputNum.get())
    if(total == 0):
        total = current * 1
    else:
        total = current * total
    inputNum.delete(0, END)
def divideClick():
    global mathType
    global total
    mathType = 4
    current = int(inputNum.get())
    if(total == 0):
        total = current / 1
    else:
        total = current / total   
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
button0 = Button(root, text="0", padx=89, pady=20, command=lambda: numberClick(0))
clearButton = Button(root, text="Clear", padx=75, pady=20, command=clearClick)
addButton = Button(root, text="+", padx=39, pady=20, command=addClick)
equalButton = Button(root, text="=", padx=39, pady=20, command=equalClick)
clearAllButton = Button(root, text="CA", padx=85, pady=20, command=clearAllClick)
subtractButton = Button(root, text="-", padx=39, pady=20, command=subtractClick)
multiplyButton = Button(root, text="x", padx=39, pady=20, command=multiplyClick)
divideButton = Button(root, text="/", padx=40, pady=20, command=divideClick)



inputNum.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0, columnspan=2)
clearButton.grid(row=5, column=2, columnspan=2)
equalButton.grid(row=4, column=2, columnspan=1)
clearAllButton.grid(row=5, column=0, columnspan=2)
addButton.grid(row=1, column=3)
subtractButton.grid(row=2, column=3)
multiplyButton.grid(row=3, column=3)
divideButton.grid(row=4, column=3)




root.mainloop()