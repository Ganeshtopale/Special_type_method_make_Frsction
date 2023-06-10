from tkinter import *
root=Tk()
fm=Frame(root)
fm.pack(fill=BOTH)
Button(fm,text="Button1",fg="red").pack()
Button(fm,text="Button2",fg="green").pack(side=RIGHT)
Button(fm,text="Button3",fg="blue").pack(side=LEFT)
root.mainloop()