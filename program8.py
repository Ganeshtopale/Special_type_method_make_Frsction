from tkinter import *

root = Tk()
root.geometry("655x333")
def cut():
    print("hello this is Cut Button")



frame = Frame(root, borderwidth=6, bg="gray", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Cut", command=cut)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="green", text="Print")
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="blue", text="Copy")
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="pink", text="Paste")
b4.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="white", text="Name")
b4.pack(side=LEFT, padx=23)
root.mainloop()
