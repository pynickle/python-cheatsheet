import tkinter

top = tkinter.Tk()
top.geometry('500x300')   # change the size
top.title("tkinter example")   # change the title

l = tkinter.Label(top, text='Hello, tkinter!', font=('monospace', 12), width=30, height=2)
l.pack()   # remember to pack

top.mainloop()