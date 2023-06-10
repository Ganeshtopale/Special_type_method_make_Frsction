from tkinter import *
main =Tk()
main.mainloop()

from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcom to check button is properly working")
window.geometry('500x300')
rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=0, row=1)
rad3.grid(column=0, row=2)
window.mainloop()