from tkinter import *

def display():
    if(x.get() == 1):
        print("agree")
    else:
        print("disagree")

win = Tk()

photo = PhotoImage(file='images\priest1_v1_1.png')

x =IntVar() #Boolean as well

check_btn = Checkbutton(win, 
                        text="I agree with everything",
                        variable = x, 
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        fg='#00FF00',
                        bg='black',
                        font=("Times New Roman", 12),
                        activeforeground= '#00FF00',
                        activebackground= 'black',
                        padx=25,
                        pady=10,
                        image=photo,
                        compound = 'left')
check_btn.pack()

win.mainloop()