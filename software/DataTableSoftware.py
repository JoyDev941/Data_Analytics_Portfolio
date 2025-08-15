from tkinter import *
import re
import os

def pos(hv):

    x = re.split("x", hv, 1)
    h, v = (int(x[0])/2), (int(x[1])/2) # center of coordinates.
    
    return h,v


def getscreensize():

    root = Tk()
    v = root.winfo_screenwidth() # 1920
    h = root.winfo_screenheight() # 1080
    root.destroy()
    
    return str(v)+"x"+str(h)

def main():
    hv = getscreensize()
    win = Tk()
    win.title("Data table software")
    win.geometry(hv)
    win.resizable(False, False)
    win.config(background="#D7E107") # set background color
    icon = PhotoImage(file="images\Icon.png") # convert icon to a tkinter format
    win.iconphoto(True, icon) # use converted icon

    label = Label(win, text="Welcome!",font=('Arial', 40, 'bold'), bg='green'); label.pack(); h,v = pos(hv); label.place(x=h*0.85, y=v*0.85)
   

    win.mainloop()

