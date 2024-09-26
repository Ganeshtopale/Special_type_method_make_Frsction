from tkinter import*
from tkinter.ttk import*
from time import strftime

root=Tk()
root.title("clock")
def time():
    string = strftime('%D/%M/%Y , %H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)
label = Label(root,font=("ds-digital",20),background="white",foreground="green")
label.pack(anchor='center')
time()
#date()
mainloop()
