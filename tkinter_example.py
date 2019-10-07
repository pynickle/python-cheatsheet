import tkinter

top = tkinter.Tk()
top.geometry('500x300')
top.title("tkinter example")

l = tkinter.Label(top, text='Hello, tkinter!', font=('monospace', 12), width=30, height=2)
l.pack()

top.mainloop()