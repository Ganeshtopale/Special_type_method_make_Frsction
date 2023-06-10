from tkinter import *
root=Tk()
label1=Label(root,text="username")
label2=Label(root,text="Password")
label1.grid(row=0)
label2.grid(row=1)
entry1=Entry(root)
entry2=Entry(root)
entry1.grid(row=0 ,column=1)
entry2.grid(row=1 ,column=1)
root.mainloop()

