from tkinter import *
import re


def pos(hv):

    x = re.split("x", hv, 1)
    h, v = (float(x[0])*0.9), (float(x[1])*0.85) # center of coordinates.
    
    return h,v

# to check screen size and to return the 
def getscreensize():

    root = Tk()
    v = root.winfo_screenwidth() # 1920
    h = root.winfo_screenheight() # 1080
    root.destroy()
    
    return str(int(0.7*v))+"x"+str(int(h*0.7))

def main():

    def click():
        var = entry1.get()
        print(var)


    hv = getscreensize()
    h,v = pos(hv)
    win = Tk()
    win.title("Data table software")
    win.geometry(hv)
    win.resizable(False, False) #locks window from resizing
    win.config(background="#D7E107") # set background color
    icon = PhotoImage(file="images\Icon.png") # convert icon to a tkinter format
    photo = PhotoImage(file="images\priest1_v1_1.png") # any time adding a image, we need to convert the photo format.
    win.iconphoto(True, icon) # use converted icon

    #label modification
    # welcome_label = Label( #this label is just liek a text box. you can design it as you please
    #     win, text="Welcome!", #what you write in the box
    #     font=('Arial', 10, 'bold'), #font design
    #     bg='green', #background of the label 
    #     relief=RAISED, # to make the label pop out.
    #     bd=10, #This increses border
    #     image=photo, #inserts an image in the software
    #     compound='top' #places the image in designated space
    #     ).place(x=h-30, y=v) # location of label
    


    entry1 = Entry(win,
                  font=("Arial", 18)).pack()
    
    button = Button(win, text="submit", 
                    command=click, 
                    fg='yellow', 
                    bg='green',
                    image = photo,
                    compound = 'top',
                    ).place(x=h-30, y=v)


    win.mainloop()

