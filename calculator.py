from tkinter import *
root = Tk()
root.title("Addition Calculator")

e = Entry(root,bg="white", width=35, borderwidth=5,font="Arial 10 bold")
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

def buttonClick(num):
    # e.delete(0,END)
    curr = e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+ str(num))
    # e.insert(END,num)

def buttonClear():
    e.delete(0,END)

def buttonAdd():
    val1 = e.get()
    global fnum
    fnum = int(val1)
    e.delete(0,END)
    # val2 = e.get()
    # res = int(val1) + int(val2)
    # print(res)

def buttonEqual():
    var2 = e.get()
    e.delete(0,END)
    e.insert(0,fnum + int(var2))

# all buttons
but1 = Button(root, text="1",padx=40,pady=20,command=lambda: buttonClick(1))
but2 = Button(root, text="2",padx=40,pady=20,command=lambda: buttonClick(2))
but3 = Button(root, text="3",padx=40,pady=20,command=lambda: buttonClick(3))
but4 = Button(root, text="4",padx=40,pady=20,command=lambda: buttonClick(4))
but5 = Button(root, text="5",padx=40,pady=20,command=lambda: buttonClick(5))
but6 = Button(root, text="6",padx=40,pady=20,command=lambda: buttonClick(6))
but7 = Button(root, text="7",padx=40,pady=20,command=lambda: buttonClick(7))
but8 = Button(root, text="8",padx=40,pady=20,command=lambda: buttonClick(8))
but9 = Button(root, text="9",padx=40,pady=20,command=lambda: buttonClick(9))
but0 = Button(root, text="0",padx=40,pady=20,command=lambda: buttonClick(0))
butadd = Button(root, text="+",padx=39,pady=20,command=buttonAdd,bg="red")
buteq = Button(root, text="=",padx=39,pady=20,command=buttonEqual,bg="light green")
buttclear = Button(root, text="CLEAR",command=buttonClear,font="Arial 12 bold",width=27,pady=10);

# Display of buttons
but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=4,column=0)
but8.grid(row=4,column=1)
but9.grid(row=4,column=2)

butadd.grid(row=5,column=0)
but0.grid(row=5,column=1)
buteq.grid(row=5,column=2)

buttclear.grid(row=6,column=0,columnspan=3)

# End of the program
root.mainloop()