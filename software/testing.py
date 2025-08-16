import tkinter
from tkinter import *

def submit():
    var = entry.get()
    print(var)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

win = Tk()
win.geometry("1280x720")
win.config(background="#FCFFC3")

entry = Entry(win, font=("Arial", 18, 'bold'), bg='black', fg="#0ACF14", show='*')
entry.pack(side=LEFT)

btn = Button(win, font=("Arial", 18), text="submit", command=submit)
btn.pack(side=RIGHT)

btn_delete = Button(win, font=("Arial", 18), text="delete", command=delete)
btn_delete.pack(side=RIGHT)

btn_backspace = Button(win, font=("Arial", 18), text="backspace", command=backspace)
btn_backspace.pack(side=RIGHT)

win.mainloop()